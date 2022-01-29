from odoo import models, fields

class PropertyManagment(models.Model):
    _name = 'managment.building'
    _description = 'Building Record'

    name_property = fields.Char(string="Name of Property")
    gps_coordinates = fields.Integer(string="GPS Coordinates")
    nbr_blocks = fields.Integer(string="Nbr of Blocks")
    nbr_floors_block = fields.Integer(string="Nbr of Floors by Block")
    nbr_units_floor = fields.Integer(string="Nbr of Units by Floor")
    nbr_stores_ground_floor = fields.Integer(string="Nbr of Stores on the Ground Floor")
    nbr_parking_places = fields.Integer(string="Nbr of Parking Places")
    nbr_cellars = fields.Integer(string="Nbr of Cellars")
    unit_type = fields.Char(string="Unit Type" )