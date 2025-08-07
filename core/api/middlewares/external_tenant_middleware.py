import requests
from django.db import connection

class ExternalTenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant_id = request.headers.get("X-Tenant-ID")
        if not tenant_id:
            return self.get_response(request)

        # Llamar al microservicio gestor
        resp = requests.get(f"http://gestor-tenants/api/tenants/{tenant_id}")
        if resp.status_code != 200:
            return self.get_response(request)

        data = resp.json()
        schema_name = data.get("schema_name")

        # Cambiar el search_path a este schema
        with connection.cursor() as cursor:
            cursor.execute(f'SET search_path TO "{schema_name}"')

        return self.get_response(request)
