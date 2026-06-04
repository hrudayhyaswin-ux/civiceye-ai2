# Copyright (C) 2026 Swecha
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file in the project root for full license information.

from flask import Flask
from flask_cors import CORS

from .config import Config
from .extensions import init_database
from .routes.admin_routes import admin_bp
from .routes.auth_routes import auth_bp
from .routes.complaint_routes import complaint_bp
from .routes.health_routes import health_bp
from .utils.response import fail


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)

    init_database(app.config["DATABASE_PATH"])

    @app.errorhandler(Exception)
    def handle_exception(e):
        # Log the error for the developer
        app.logger.error(f"Unhandled Exception: {e}", exc_info=True)
        return fail(str(e), 500)

    app.register_blueprint(health_bp)
    app.register_blueprint(complaint_bp, url_prefix="/api")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    @app.get("/api/uploads/media/<filename>")
    def serve_media(filename):
        import os

        from flask import send_from_directory
        upload_dir = os.path.join(app.root_path, "..", "uploads", "media")
        return send_from_directory(upload_dir, filename)

    return app

