from rolepermissions.roles import AbstractUserRole

class Barbeiro(AbstractUserRole):
    available_permissions = {'criar_agenda':True, 'criar_horarios':True, 'concluir_agenda':True, 'ver_cliente':True, 'ver_feedback':True}
    
class Cliente(AbstractUserRole):
    available_permissions = {'agendar':True, 'ver_historico':True, 'criar_pedido':True, 'horarios':True, 'ver_feedback':True, 'addfeed':True, 'enviarfeed':True , 'datas':True, 'horarios':True}