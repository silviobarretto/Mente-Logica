# Para acessar uma área restrita, o usuário deve inserir a senha correta e não pode estar bloqueado.
# Dados:
# Senha inserida: "abcd1234"
# Senha correta: "abcd1234"
# Usuário bloqueado: False
# Verifique se o acesso deve ser concedido.

senhaInserida = 'abcd1234'
senhaCorreta = 'abcd1234'
usuarioBloqueado = False

acessoLiberado = (senhaInserida == senhaCorreta) and not usuarioBloqueado

print('Você está logado?', acessoLiberado)
