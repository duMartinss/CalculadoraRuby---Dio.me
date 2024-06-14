class Mercado
    def initialize(nome, preco)
        @nome = nome
        @preco = preco
    end

    def comprar
        puts "Você comprou o produto #{@nome} pelo valor de R$#{@preco}."
    end
end