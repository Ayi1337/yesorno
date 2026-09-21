import os

from server import APIError, Handler, JevClient


class handler(Handler):
    def check_origin(self):
        host = self.headers.get("Host", "")
        origin = self.headers.get("Origin")
        if not host or (origin and origin != "https://" + host) or self.headers.get("Sec-Fetch-Site") == "cross-site":
            raise APIError(403, "forbidden", "请从本站页面提交。")

    def get_client(self):
        key = os.environ.get("TYPESAFE_API_KEY", "").strip()
        if not key or "\n" in key or "\r" in key:
            raise APIError(503, "service_configuration", "服务暂时不可用，请稍后再试。")
        self.client = JevClient(key)
        return self.client

    def do_GET(self):
        self.respond(405, {"error": {"code": "method_not_allowed", "message": "请通过页面提交问题。"}})

    def do_POST(self):
        self.client = None
        try:
            super().do_POST()
        finally:
            if self.client:
                self.client.close()
