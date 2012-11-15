# -*- coding: utf-8 -*-

# Copyright (c) 2012 theo crevon
#
# See the file LICENSE for copying permission.


from flask import Response


class Ok(Response):
    def __init__(self, *args, **kwargs):
        super(self, Ok).__init__(*args, **kwargs)

        self.status = 200


class Created(Response):
    def __init__(self, *args, **kwargs):
        super(self, Created).__init__(*args, **kwargs)

        self.status = 201


class BadRequest(Response):
    def __init__(self, *args, **kwargs):
        super(self, BadRequest).__init__(*args, **kwargs)

        self.status = 400


class NotFound(Response):
    def __init__(self, *args, **kwargs):
        super(self, NotFound).__init__(*args, **kwargs)

        self.status = 404


class Conflict(Response):
    def __init__(self, *args, **kwargs):
        super(self, Conflict).__init__(*args, **kwargs)

        self.status = 409


class MethodNotAllowed(Response):
    def __init__(self, *args, **kwargs):
        super(self, MethodNotAllowed).__init__(*args, **kwargs)

        self.status = 405


class InvalidMediaType(Response):
    def __init__(self, *args, **kwargs):
        super(self, InvalidMediaType).__init__(*args, **kwargs)

        self.status = 415


class InternalServerError(Response):
    def __init__(self, *args, **kwargs):
        super(self, InternalServerError).__init__(*args, **kwargs)

        self.status = 500


class ServiceUnavailable(Response):
    def __init__(self, *args, **kwargs):
        super(self, ServiceUnavailable).__init__(*args, **kwargs)

        self.status = 503
