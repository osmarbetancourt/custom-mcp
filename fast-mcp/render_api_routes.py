# This file will contain the route-to-operationId mapping for the Render API, based on render-open-api.json.
# Format: {"route": {"methods": ["GET", "POST", ...], "operationId": "..."}}
# This is for review and planning before code generation.

render_api_routes = [
    # Blueprints
    {"route": "/blueprints", "methods": ["GET"], "operationId": "list_blueprints"},
    {"route": "/blueprints/{blueprintId}", "methods": ["GET"], "operationId": "retrieve_blueprint"},
    {"route": "/blueprints/{blueprintId}", "methods": ["PATCH"], "operationId": "update_blueprint"},
    {"route": "/blueprints/{blueprintId}", "methods": ["DELETE"], "operationId": "disconnect_blueprint"},

    # Disks
    {"route": "/disks", "methods": ["POST"], "operationId": "add_disk"},
    {"route": "/disks/{diskId}", "methods": ["DELETE"], "operationId": "delete_disk"},
    {"route": "/disks/{diskId}/snapshots", "methods": ["GET"], "operationId": "list_snapshots"},
    {"route": "/disks/{diskId}/snapshots/restore", "methods": ["POST"], "operationId": "restore_snapshot"},
    {"route": "/disks/{diskId}", "methods": ["GET"], "operationId": "retrieve_disk"},
    {"route": "/disks/{diskId}", "methods": ["PATCH"], "operationId": "update_disk"},

    # Users
    {"route": "/users", "methods": ["GET"], "operationId": "get_user"},

    # Workspaces (Owners)
    {"route": "/owners", "methods": ["GET"], "operationId": "list_owners"},
    {"route": "/owners/{ownerId}", "methods": ["GET"], "operationId": "retrieve_owner"},
    {"route": "/owners/{ownerId}/members", "methods": ["GET"], "operationId": "retrieve_owner_members"},

    # Notification Settings
    {"route": "/notification-settings/owners/{ownerId}", "methods": ["GET"], "operationId": "retrieve_owner_notification_settings"},
    {"route": "/notification-settings/owners/{ownerId}", "methods": ["PATCH"], "operationId": "patch_owner_notification_settings"},
    {"route": "/notification-settings/overrides", "methods": ["GET"], "operationId": "list_notification_overrides"},
    {"route": "/notification-settings/overrides/services/{serviceId}", "methods": ["GET"], "operationId": "retrieve_service_notification_overrides"},
    {"route": "/notification-settings/overrides/services/{serviceId}", "methods": ["PATCH"], "operationId": "patch_service_notification_overrides"},

    # Registry Credentials
    {"route": "/registrycredentials", "methods": ["GET"], "operationId": "list_registry_credentials"},
    {"route": "/registrycredentials", "methods": ["POST"], "operationId": "create_registry_credential"},
    {"route": "/registrycredentials/{registryCredentialId}", "methods": ["DELETE"], "operationId": "delete_registry_credential"},
    {"route": "/registrycredentials/{registryCredentialId}", "methods": ["GET"], "operationId": "retrieve_registry_credential"},
    {"route": "/registrycredentials/{registryCredentialId}", "methods": ["PATCH"], "operationId": "update_registry_credential"},

    # Services (partial, add more as needed)
    {"route": "/services", "methods": ["POST"], "operationId": "create_service"},
    {"route": "/services", "methods": ["GET"], "operationId": "list_services"},
    {"route": "/services/{serviceId}", "methods": ["DELETE"], "operationId": "delete_service"},
    {"route": "/services/{serviceId}", "methods": ["GET"], "operationId": "retrieve_service"},
    {"route": "/services/{serviceId}", "methods": ["PATCH"], "operationId": "update_service"},
    # ... (repeat for all discovered endpoints in all subfolders)
]
