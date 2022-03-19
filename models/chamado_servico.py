import logging
logger = logging.getLogger(__name__)

from odoo import models, api, fields
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from datetime import datetime, date

class ChamadoServico(models.Model):
    _name = 'chamado.servico'

    funcionario = fields.Char(
        string='Funcionário',
        related = 'create_uid.name',
        index=True,
        readonly=True
    )
    
    problema = fields.Text("Especifique o problema", required=True, tracking=True)

    tipo_servico = fields.Many2one('tipo.servico', string="Tipo de Serviço", required=True)

    status = fields.Selection([
        ('aberto', 'Aberto'),
        ('analise', 'Em Análise'),
        ('resolvido', 'Resolvido'),
        ('smSolucao', 'Sem Solução'),
        ('cancelado', 'Cancelado')
    ],'Status', default='aberto', tracking=True)

    @api.model
    def validacaoMudancaStatus(self, old_state, new_state):
        permitido = [
            ('aberto', 'analise'),
            ('analise', 'resolvido'),
            ('analise', 'smSolucao'),
            ('analise', 'cancelado'),
            ('aberto', 'cancelado')
        ]
        return (old_state, new_state) in permitido

    def mudarStatus(self, new_state):
        for chamado in self:
            if chamado.validacaoMudancaStatus(chamado.status, new_state):
                chamado.status = new_state
            else:
                msg = ('Status de %s para %s não é permitido.') % (chamado.status, new_state)
                raise UserError(msg)

    data_problema = fields.Date(
        'Data do chamado',
        default = datetime.today(),
        #compute="get_date",
        readonly=True
        )
    
    data_att = fields.Date(
        'Data de atualização',
        default = datetime.today(),
        readonly=True
        )

    def data_atualizacao(self):
        hoje = fields.datetime.today()
        return hoje
    
    def fazerAberto(self):
        self.mudarStatus('aberto')
        self.write({
            "data_att": self.data_atualizacao()
        })

    def fazerAnalise(self):
        self.mudarStatus('analise')
        self.write({
            "data_att": self.data_atualizacao()
        })

    def fazerResolvido(self):
        self.mudarStatus('resolvido')
        self.write({
            "data_att": self.data_atualizacao()
        })

    def fazerSolucao(self):
        self.mudarStatus('smSolucao')
        self.write({
            "data_att": self.data_atualizacao()
        })

    def fazerCancelado(self):
        self.mudarStatus('cancelado')
        self.write({
            "data_att": self.data_atualizacao()
        })




    #@api.depends("data_atualizacao")
    #def get_date(self):
    #    hoje = fields.datetime.today()
    #    #if len(str(self.data_problema)) < 8:
    #    #    self.data_problema=hoje
    #    #else:
    #    #    self.data_problema=self.data_problema
    #    for problema in self:
    #        if problema.data_problema == False:
    #            problema.data_problema = hoje
    #        else:
    #            return problema.data_problema

    
