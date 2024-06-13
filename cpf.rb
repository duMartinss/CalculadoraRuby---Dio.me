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


