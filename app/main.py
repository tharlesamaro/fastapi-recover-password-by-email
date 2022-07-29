from fastapi import FastAPI

app_kwargs = {
    "name": "",
    "description": "",
    "version": "",
    "env": "",
}

app = FastAPI(**app_kwargs)
app.add_api_route("/", lambda: app_kwargs, include_in_schema=False)

add_exception_handlers(app)
add_middlewares(app)
add_routes(app)
