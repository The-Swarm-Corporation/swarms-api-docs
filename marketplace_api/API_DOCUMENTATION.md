# Prompt Marketplace API Documentation

## Overview
Users can add prompts to the marketplace via two API endpoints with a daily limit of 500 prompts per user.

## Rate Limiting
- **Daily Limit**: 500 prompts per user per day
- **Reset Time**: Midnight UTC
- **Free Content**: 500 free prompts per day
- **Paid Content**: 500 paid prompts per day

## API Endpoints

### 1. REST API Endpoints

#### Add Prompt
**URL**: `POST /api/add-prompt`

**Authentication**: 
- API Key (Bearer token) in Authorization header
- OR Supabase session authentication

**Request Body**:
```json
{
  "name": "string (min 2 characters)",
  "prompt": "string (min 5 characters)",
  "description": "string (optional)",
  "useCases": [
    {
      "title": "string (required)",
      "description": "string (required)"
    }
  ],
  "tags": "string (comma-separated)",
  "is_free": "boolean (default: true)",
  "price_usd": "number (required if is_free: false)",
  "category": "string (optional)",
  "status": "string (default: 'pending')",
  "tokenized_on": "boolean (optional)",
  "image_url": "string (optional, must be valid URL)",
  "file_path": "string (optional)",
  "links": [
    {
      "name": "string",
      "url": "string (valid URL)"
    }
  ],
  "seller_wallet_address": "string (optional, required for paid prompts)"
}
```

**Response**:
```json
{
  "success": true,
  "id": "uuid",
  "listing_url": "https://swarms.world/prompt/{id}"
}
```

**Error Responses**:
- `400`: Validation errors, content validation failed
- `401`: Authentication required
- `429`: Daily limit exceeded
- `500`: Server error

#### Update Prompt
**URL**: `POST /api/edit-prompt`

**Authentication**: 
- API Key (Bearer token) in Authorization header
- OR Supabase session authentication

**Request Body**:
```json
{
  "id": "string (required, prompt ID to update)",
  "name": "string (min 2 characters)",
  "prompt": "string (min 5 characters)",
  "description": "string (optional)",
  "useCases": [
    {
      "title": "string (required)",
      "description": "string (required)"
    }
  ],
  "tags": "string (comma-separated)",
  "is_free": "boolean (optional)",
  "price_usd": "number (required if is_free: false)",
  "category": "array of strings (optional)",
  "status": "string (optional)",
  "image_url": "string (optional, must be valid URL)",
  "file_path": "string (optional)",
  "links": [
    {
      "name": "string",
      "url": "string (valid URL)"
    }
  ],
  "seller_wallet_address": "string (optional, required for paid prompts)",
  "tokenized_on": "boolean (optional)"
}
```

**Response**:
```json
{
  "success": true,
  "id": "uuid",
  "listing_url": "https://swarms.world/prompt/{id}",
  "updated_data": { /* updated prompt data */ }
}
```

### 2. tRPC Endpoints

#### Add Prompt
**Procedure**: `explorer.addPrompt`

**Authentication**: Supabase session required

**Input Schema**: Same as REST API request body

**Response**: 
```json
{
  "id": "uuid",
  "listing_url": "https://swarms.world/prompt/{id}"
}
```

#### Update Prompt
**Procedure**: `explorer.updatePrompt`

**Authentication**: Supabase session required

**Input Schema**: Same as REST API request body (with required `id` field)

**Response**: 
```json
{
  "success": true,
  "id": "uuid",
  "listing_url": "https://swarms.world/prompt/{id}"
}
```

**Error Responses**:
- `TOO_MANY_REQUESTS`: Daily limit exceeded
- `FORBIDDEN`: Content validation failed
- `BAD_REQUEST`: Validation errors

## Usage Examples

### REST API with API Key
```bash
curl -X POST http://localhost:3000/api/add-prompt \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "name": "My Prompt",
    "prompt": "This is my prompt content",
    "description": "A useful prompt for various tasks",
    "useCases": [
      {
        "title": "Content Generation",
        "description": "Generate creative content"
      }
    ],
    "tags": "content,generation,creative",
    "is_free": true,
    "category": "content"
  }'
```

### REST API with Supabase Session
```bash
curl -X POST http://localhost:3000/api/add-prompt \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer SUPABASE_SESSION_TOKEN" \
  -d '{...}'
```

### Update Prompt via REST API
```bash
curl -X POST http://localhost:3000/api/edit-prompt \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "id": "prompt-uuid-here",
    "name": "Updated Prompt Name",
    "prompt": "Updated prompt content...",
    "description": "Updated description",
    "image_url": "https://example.com/new-image.jpg",
    "tags": "updated,tags,here"
  }'
```

## Rate Limit Information

When the daily limit is exceeded, the API returns:

```json
{
  "error": "Daily limit exceeded",
  "message": "Daily limit reached: 500 prompts per day. Resets at midnight.",
  "currentUsage": {
    "paidPrompts": 500,
    "paidAgents": 0,
    "freeContent": 0,
    "date": "2024-01-01"
  },
  "limits": {
    "paidPrompts": 500,
    "paidAgents": 3,
    "freeContent": 500
  },
  "resetTime": "2024-01-02T00:00:00.000Z"
}
```

## Content Validation

All prompts go through fraud prevention and content validation:
- Duplicate content detection
- Quality assessment
- Trustworthiness scoring

## Database Schema

Prompts are stored in the `swarms_cloud_prompts` table with the following key fields:
- `id`: UUID primary key
- `user_id`: UUID foreign key to users table
- `name`: Prompt name
- `prompt`: Prompt content
- `description`: Optional description
- `use_cases`: JSON array of use cases
- `tags`: Comma-separated tags
- `is_free`: Boolean for free/paid status
- `price_usd`: USD price (for paid prompts)
- `price`: SOL price (calculated from USD)
- `category`: Optional category
- `status`: pending/approved/rejected
- `created_at`: Timestamp
- `tokenized_on`: Boolean for tokenization status

## Implementation Notes

1. **Rate Limiting**: Implemented in `shared/utils/api/daily-rate-limit.ts`
2. **Authentication**: Uses `HybridAuthGuard` for flexible auth
3. **Validation**: Uses `validateMarketplaceSubmission` for content validation
4. **Price Conversion**: Automatically converts USD to SOL using current market price
5. **Duplicate Prevention**: Checks for existing prompts with same content and user
