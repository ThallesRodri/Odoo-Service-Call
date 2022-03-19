{
    'name': "Chamados TI",
    'summary': "Organização de chamados para o setor TI",     
    'author': "Thalles Rodrigues",
    'website': "https://vidroshima.com.br/",
    'category': 'Uncategorized',
    'version': '14.0.1.0.0',
    'depends': ['base'],
    'data': [ 
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/chamado_servico_view.xml",
        "views/tipo_servico_view.xml",
        ],
    #'demo': ['demo.xml'],
    'installable': True,
    'application': True,
}