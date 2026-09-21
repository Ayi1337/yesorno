import os

from server import Handler, MODEL


class handler(Handler):
    def do_GET(self):
        ready = bool(os.environ.get("TYPESAFE_API_KEY", "").strip())
        self.respond(200 if ready else 503, {"ready": ready, "model": MODEL})

    def do_POST(self):
        self.respond(405, {"error": {"code": "method_not_allowed", "message": "接口不支持此操作。"}})
