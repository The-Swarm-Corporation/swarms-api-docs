# Swarms Platform API Reference

## Overview

The Swarms Platform provides a simple API for managing AI prompts and agents in the marketplace. The API supports both REST endpoints and tRPC procedures with hybrid authentication (API keys and Supabase sessions).

## Base URLs

- **Production**: `https://swarms.world`
- **Development**: `http://localhost:3000`

## Authentication

The API supports two authentication methods:

1. **API Key Authentication**: Include your API key in the `Authorization` header as `Bearer <your-api-key>`
2. **Supabase Session**: Include your Supabase session token in the `Authorization` header

## Rate Limiting

- **Daily Limits**: 500 prompts/agents per user per day
- **Reset Time**: Midnight UTC

## Error Handling

All endpoints return consistent error responses:

```json
{
  "error": "Error message",
  "message": "Detailed error description",
  "code": "ERROR_CODE"
}
```

Common HTTP status codes:
- `200`: Success
- `400`: Bad Request (validation errors)
- `401`: Unauthorized (authentication required)
- `403`: Forbidden (insufficient permissions)
- `404`: Not Found
- `429`: Too Many Requests (rate limit exceeded)
- `500`: Internal Server Error

---

## REST API Endpoints

#### Add Prompt
**POST** `/api/add-prompt`

Creates a new prompt in the marketplace.

**Authentication**: Required (API Key or Supabase session)

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
  "price_usd": "number (required if is_free: false, min: 0.01)",
  "category": "string (optional)",
  "status": "string (default: 'pending')",
  "tokenized_on": "boolean (optional)",
  "image_url": "string (optional, must be valid URL)",
  "file_path": "string (optional)",
  "links": ["string (optional)"],
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

#### Add Agent
**POST** `/api/add-agent`

Creates a new agent in the marketplace.

**Authentication**: Required (API Key or Supabase session)

**Request Body**:
```json
{
  "name": "string (min 2 characters)",
  "agent": "string (min 5 characters)",
  "language": "string (optional)",
  "description": "string (required)",
  "requirements": [
    {
      "package": "string",
      "installation": "string"
    }
  ],
  "useCases": [
    {
      "title": "string",
      "description": "string"
    }
  ],
  "tags": "string (comma-separated)",
  "is_free": "boolean (default: true)",
  "price_usd": "number (required if is_free: false, min: 0.01)",
  "category": "string (optional)",
  "status": "string (default: 'pending')",
  "tokenized_on": "boolean (optional)",
  "image_url": "string (optional, must be valid URL)",
  "file_path": "string (optional)",
  "links": ["string (optional)"],
  "seller_wallet_address": "string (optional, required for paid agents)"
}
```

**Response**:
```json
{
  "success": true,
  "id": "uuid",
  "listing_url": "https://swarms.world/agent/{id}"
}
```

#### Edit Prompt
**POST** `/api/edit-prompt`

Updates an existing prompt.

**Authentication**: Required (API Key or Supabase session)

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
  "category": "string (optional)",
  "status": "string (optional)",
  "image_url": "string (optional, must be valid URL)",
  "file_path": "string (optional)",
  "links": ["string (optional)"],
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

#### Edit Agent
**POST** `/api/edit-agent`

Updates an existing agent.

**Authentication**: Required (API Key or Supabase session)

**Request Body**: Similar to add-agent with additional `id` field

**Response**:
```json
{
  "success": true,
  "id": "uuid",
  "listing_url": "https://swarms.world/agent/{id}",
  "updated_data": { /* updated agent data */ }
}
```

### Query Endpoints

#### Query Agents
**POST** `/api/query-agents`

Searches and filters agents.

**Request Body**:
```json
{
  "search": "string (optional)",
  "category": "string (optional)",
  "priceFilter": "string (optional, 'all', 'free', 'paid')",
  "userFilter": "string (optional)",
  "sortBy": "string (optional, 'newest', 'oldest', 'popular', 'rating')",
  "limit": "number (default: 6)",
  "offset": "number (default: 0)"
}
```

#### Query Prompts
**POST** `/api/query-prompts`

Searches and filters prompts in the marketplace.

**Authentication**: Optional

**Request Body**:
```json
{
  "search": "string (optional, max 100 characters)",
  "category": "string (optional, max 50 characters)",
  "priceFilter": "string (optional, 'all', 'free', 'paid')",
  "userFilter": "string (optional, user ID)",
  "sortBy": "string (optional, 'newest', 'oldest', 'popular', 'rating')",
  "limit": "number (optional, min: 1, max: 100, default: 6)",
  "offset": "number (optional, min: 0, default: 0)"
}
```

**Response**:
```json
[
  {
    "id": "string",
    "name": "string",
    "prompt": "string",
    "description": "string",
    "use_cases": [
      {
        "title": "string",
        "description": "string"
      }
    ],
    "tags": "string",
    "is_free": "boolean",
    "price_usd": "number",
    "price": "number",
    "category": "string",
    "status": "string",
    "tokenized_on": "boolean",
    "image_url": "string",
    "file_path": "string",
    "links": ["string"],
    "seller_wallet_address": "string",
    "user_id": "string",
    "created_at": "string",
    "updated_at": "string"
  }
]
```

**Error Responses**:
- `400`: Validation errors
- `500`: Server error

**Query Parameters**:
- `search`: Search in prompt name and description
- `category`: Filter by category (case-insensitive)
- `priceFilter`: 
  - `'all'`: Show all prompts (default)
  - `'free'`: Show only free prompts
  - `'paid'`: Show only paid prompts
- `userFilter`: Filter by specific user ID
- `sortBy`:
  - `'newest'`: Sort by creation date (newest first)
  - `'oldest'`: Sort by creation date (oldest first)
  - `'popular'`: Sort by popularity/rating
  - `'rating'`: Sort by average rating
- `limit`: Number of results to return (1-100)
- `offset`: Number of results to skip for pagination

**Example Request**:
```bash
curl -X POST https://swarms.world/api/query-prompts \
  -H "Content-Type: application/json" \
  -d '{
    "search": "data analysis",
    "category": "development",
    "priceFilter": "all",
    "sortBy": "newest",
    "limit": 10,
    "offset": 0
  }'
```

**Example Response**:
```json
[
  {
    "id": "prompt-123",
    "name": "Data Analysis Assistant",
    "prompt": "You are a data analysis expert who helps users analyze datasets...",
    "description": "An AI assistant specialized in data analysis and visualization",
    "use_cases": [
      {
        "title": "Data Cleaning",
        "description": "Help clean and preprocess datasets"
      },
      {
        "title": "Statistical Analysis",
        "description": "Perform statistical analysis on data"
      }
    ],
    "tags": "data,analysis,python,statistics",
    "is_free": true,
    "price_usd": null,
    "price": null,
    "category": "development",
    "status": "approved",
    "tokenized_on": false,
    "image_url": "https://example.com/image.jpg",
    "file_path": null,
    "links": ["https://github.com/example/repo"],
    "seller_wallet_address": null,
    "user_id": "user-456",
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z"
  }
]
```

---

## tRPC Procedures

### Explorer Router (`explorer.*`)

#### Add Prompt
**Procedure**: `explorer.addPrompt`

Creates a new prompt.

**Input**: Same as REST API add-prompt

**Response**:
```typescript
{
  id: string,
  listing_url: string
}
```

#### Update Prompt
**Procedure**: `explorer.updatePrompt`

Updates an existing prompt.

**Input**: Same as REST API edit-prompt

**Response**:
```typescript
{
  success: boolean,
  id: string,
  listing_url: string
}
```

#### Add Agent
**Procedure**: `explorer.addAgent`

Creates a new agent.

**Input**: Similar to add-prompt with agent-specific fields

**Response**:
```typescript
{
  id: string
}
```

#### Update Agent
**Procedure**: `explorer.updateAgent`

Updates an existing agent.

**Input**: Similar to edit-prompt with agent-specific fields

**Response**:
```typescript
{
  success: boolean
}
```

#### Get All Prompts
**Procedure**: `explorer.getAllPrompts`

Retrieves all prompts with pagination.

**Input**:
```typescript
{
  limit: number (default: 6),
  offset: number (default: 1),
  search: string (optional)
}
```

#### Get User Prompts
**Procedure**: `explorer.getUserPrompts`

Retrieves prompts for the authenticated user.

**Response**: Array of prompts

#### Get Prompt by ID
**Procedure**: `explorer.getPromptById`

Retrieves a specific prompt by ID.

**Input**: `string` (prompt ID)

#### Get All Agents
**Procedure**: `explorer.getAllAgents`

Retrieves all agents.

#### Get Agent by ID
**Procedure**: `explorer.getAgentById`

Retrieves a specific agent by ID.

**Input**: `string` (agent ID)

#### Get Agents by User ID
**Procedure**: `explorer.getAgentsByUserId`

Retrieves agents for a specific user.

**Input**: `string` (user ID)

#### Validate Prompt
**Procedure**: `explorer.validatePrompt`

Validates prompt content and checks for duplicates.

**Input**:
```typescript
{
  prompt: string,
  editingId: string (optional)
}
```

**Response**:
```typescript
{
  valid: boolean,
  error: string
}
```

#### Validate Agent
**Procedure**: `explorer.validateAgent`

Validates agent content and checks for duplicates.

**Input**:
```typescript
{
  agent: string,
  editingId: string (optional)
}
```

**Response**:
```typescript
{
  valid: boolean,
  error: string
}
```

#### Get Agent Tags
**Procedure**: `explorer.getAgentTags`

Retrieves available agent categories/tags.

**Response**:
```typescript
{
  categories: string[]
}
```

---

## Data Models

### Prompt
```typescript
interface Prompt {
  id: string;
  name: string;
  prompt: string;
  description?: string;
  use_cases: UseCase[];
  tags?: string;
  is_free: boolean;
  price_usd?: number;
  price?: number; // SOL price
  category?: string;
  status: 'pending' | 'approved' | 'rejected';
  tokenized_on?: boolean;
  token_address?: string;
  pool_address?: string;
  image_url?: string;
  file_path?: string;
  links?: string[];
  seller_wallet_address?: string;
  user_id: string;
  created_at: string;
  updated_at: string;
}
```

### Agent
```typescript
interface Agent {
  id: string;
  name: string;
  agent: string;
  description: string;
  language?: string;
  requirements: Requirement[];
  use_cases: UseCase[];
  tags?: string;
  is_free: boolean;
  price_usd?: number;
  price?: number; // SOL price
  category?: string;
  status: 'pending' | 'approved' | 'rejected';
  tokenized_on?: boolean;
  token_address?: string;
  pool_address?: string;
  image_url?: string;
  file_path?: string;
  links?: string[];
  seller_wallet_address?: string;
  user_id: string;
  created_at: string;
  updated_at: string;
}
```

### UseCase
```typescript
interface UseCase {
  title: string;
  description: string;
}
```

### Requirement
```typescript
interface Requirement {
  package: string;
  installation: string;
}
```

---

## Examples

### Creating a Prompt with API Key
```bash
curl -X POST https://swarms.world/api/add-prompt \
  -H "Authorization: Bearer your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Code Review Assistant",
    "prompt": "Review the following code and provide suggestions for improvement",
    "description": "An AI assistant that reviews code and provides constructive feedback",
    "useCases": [
      {
        "title": "Code Quality Review",
        "description": "Review code for bugs, performance issues, and best practices"
      }
    ],
    "tags": "code,review,assistant,programming",
    "is_free": true,
    "category": "development"
  }'
```

### Creating an Agent with tRPC
```typescript
const agent = await trpc.explorer.addAgent.mutate({
  name: "Data Analysis Agent",
  agent: "You are a data analysis expert...",
  description: "An AI agent specialized in data analysis and visualization",
  requirements: [
    {
      package: "pandas",
      installation: "pip install pandas"
    }
  ],
  useCases: [
    {
      title: "Data Cleaning",
      description: "Clean and preprocess datasets"
    }
  ],
  tags: "data,analysis,python,ml",
  is_free: false,
  price_usd: 9.99,
  seller_wallet_address: "your-wallet-address"
});
```

### Querying Prompts
```bash
curl -X POST https://swarms.world/api/query-prompts \
  -H "Content-Type: application/json" \
  -d '{
    "search": "data analysis",
    "category": "development",
    "priceFilter": "all",
    "sortBy": "newest",
    "limit": 10,
    "offset": 0
  }'
```

### Querying Agents
```bash
curl -X POST https://swarms.world/api/query-agents \
  -H "Content-Type: application/json" \
  -d '{
    "search": "machine learning",
    "category": "ai",
    "priceFilter": "free",
    "sortBy": "popular",
    "limit": 5,
    "offset": 0
  }'
```

---

## Support

For API support and questions:
- **Documentation**: [https://swarms.world/docs](https://swarms.world/docs)
- **GitHub**: [https://github.com/swarms-ai/swarms-platform](https://github.com/swarms-ai/swarms-platform)
- **Discord**: [https://discord.gg/swarms](https://discord.gg/swarms)

---