from odoo import models, api, fields

class TipoServico(models.Model):
    _name = "tipo.servico"
    _description = "Tipos de Serviços"
    _rec_name = "nome"
    
    nome = fields.Char("Tipo de Serviços", tracking=True)