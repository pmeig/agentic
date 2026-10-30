# Code analysis for documentation: routes and handlers

## Routes and handlers (what to grep)

| Stack | Pattern |
|---|---|
| Fastify/Express | `\.(get\|post\|put\|patch\|delete)\(` , `register(`, route files |
| NestJS | `@Controller(`, `@Get(`, `@Post(`... |
| Spring | `@(Rest)?Controller`, `@(Get\|Post\|Put\|Delete\|Request)Mapping` |
| Ktor | `routing {`, `get("`, `post("` |
| FastAPI/Flask/Django | `@app.(get\|post)`, `@router.`, `urlpatterns`, `path(` |
| ASP.NET | `[ApiController]`, `[Http(Get\|Post)]`, `MapGet(` |
| Go | `HandleFunc(`, `r.(Get\|Post)(`, `e.(GET\|POST)(` |
| Angular | `Routes`, `loadComponent`, `path:` in `*.routes.ts` |
| Android Compose | `NavHost`, `composable(`, route constants |
| Jobs/events | `@Scheduled`, `cron`, `@MessagePattern`, `subscribe(` |
Record `METHOD path | file:line | auth | feature`; `doc-openapi-asyncapi` turns it into the contract.
