// NOMES: Ian Miranda Da Cunha, Vinicius Serpa Pansan, João Pedro Zavanela Andreu
// TIAs: 42227161, 42230306, 42246271
#include <locale.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define max 1000
#define Dicionario "texto.txt"
#define caracteres 100


char minusculo(char character) {
    return (character >= 'A' && character <= 'Z') ? (character + ('a' - 'A')) : character;
}

int comparar(char s1[caracteres], char s2[caracteres]) {
    int i = 0;

    while (s1[i] && s2[i] && minusculo(s1[i]) ==  minusculo(s2[i]))
        i++;

    return s1[i] - s2[i];
}

void add(char palavra[caracteres], char dicionario[max][caracteres], int *num_palavras) {
    int inicio = 0;
    int fim = *num_palavras - 1;
    int meio;

    while (inicio <= fim) {
        meio = (inicio + fim) / 2;

        int comparacao = comparar(palavra, dicionario[meio]);

        if (comparacao == 0)
            return;
        else if (comparacao < 0)
            fim = meio - 1;
        else
            inicio = meio + 1;
    }

    for (int j = *num_palavras; j > inicio; j--)
        strcpy(dicionario[j], dicionario[j - 1]);

    strcpy(dicionario[inicio], palavra);
    (*num_palavras)++;
}

int main() {
    setlocale(LC_ALL, "Portuguese");

    char dicionario[max][caracteres];
    int num_palavras = 0;
    char palavra[caracteres];

    FILE *arquivo = fopen(Dicionario, "r");

    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo.\n");
        return 1;
    }

    while (fscanf(arquivo, "%s", palavra) != EOF) {
        for (int i = 0; palavra[i]; i++)
            palavra[i] = minusculo(palavra[i]);

        add(palavra, dicionario, &num_palavras);
    }

    for (int i = 0; i < num_palavras; i++)
        printf("%s\n", dicionario[i]);

    printf("Total de palavras no dicionário = %d\n", num_palavras);

    fclose(arquivo);

    return 0;
}
