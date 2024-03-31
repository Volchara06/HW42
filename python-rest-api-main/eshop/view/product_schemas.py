from marshmallow import Schema, fields


class ProductCreateDtoSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class ProductGetManyParams(Schema):
    page = fields.Int(required=True)
    limit = fields.Int(required=True)


class ProductSchema(Schema):
    id = fields.String()
    name = fields.String()
    price = fields.Float()
