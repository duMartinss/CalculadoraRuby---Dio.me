require_relative 'mercado.rb'
require_relative 'produtos.rb'

produtos = Produtos.new
produtos.nome = 'Arroz 2Kg'
produtos.preco = 25

Mercado.new(produtos.nome,produtos.preco).comprar