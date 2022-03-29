# Numeric base converter

<!--
https://terminaldeinformacao.com/2013/01/18/conversao-de-bases/
-->

## Fórmulas

Converter primeiro a base numérica corrente para decimal para então convertê-la para a base binária foi a estratégia adotada no decorrer deste trabalho. Assim pôde-se realizar um melhor reaproveito do código fonte desenvolvido.

### Converter base para decimal

- Fórmula

    $$
    \sum_{i=1}^n (d_{n-i} * b ^ {n-i}) =
        d_{n-0} * b^{n-0} +
        d_{n-1} * b^{n-1} +
        d_{n-2} * b^{n-2} +
        ... +
        d_{0} * b^{0}
        d_{-1} * b^{-1} +
        d_{-2} * b^{-2} +
        ...
    $$

    - Para $b = 10$

- Legenda
    |Sigla  |Descrição
    |---    |---
    |d      |Algarismo
    |b      |Base numérica
    |n      |Iteração

- Exemplo de conversão do número $ (257)_{8} $ para decimal

    1. Realizar o cálculo do somatório da multiplicação dos algarismos pela base elevada pela iteração.

        ```math
        7 * 8 ^ 0 = 7
        5 * 8 ^ 1 = 40
        2 * 8 ^ 2 = 128

        soma = 7 + 40 + 128
        soma = 175
        ```

### Converter base para base binária

1. Certificar de que o número esteja na base númerica decimal.

1. Aplicar a seguinte fórmula

$$
???
$$

### Converter base para base octal (ARRUMAR)

1. Certificar de que o número esteja na base númerica decimal.

1. Aplicar a seguinte fórmula

    $$
    \sum_{i=1}^n (d_{n-i} * b ^ {n-i}) =
        d_{n-0} * b^{n-0} +
        d_{n-1} * b^{n-1} +
        d_{n-2} * b^{n-2} +
        ... +
        d_{0} * b^{0}
        d_{-1} * b^{-1} +
        d_{-2} * b^{-2} +
        ...
    $$