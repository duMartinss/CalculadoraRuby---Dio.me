#Validar CPF.
#Ponha 'gem install cpf_cnpj' no terminal e instale a gem.
#Não se esqueça de digitar o require no começo do seu código.
#Gem do desenvolvedor Nando Vieira, (https://rubygems.org/gems/cpf_cnpj).

require 'cpf_cnpj'

print "Digite o seu cpf: "
cpf = gets.chomp.to_i


def validarCpf(cpf)
    CPF.valid?(cpf)
end


if validarCpf(cpf)
    puts "Cpf válido"
else
    puts "Cpf inválido" 
end


