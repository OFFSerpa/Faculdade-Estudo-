#include <stdio.h>
#include <stdbool.h>

void imprimir(char m[3][3]) {
    printf("\n  1 2 3\n");
    for (int i = 0; i < 3; i++) {
        printf("%d > ", i + 1);
        for (int j = 0; j < 3; j++) {
            printf("%c|", m[i][j]);
        }
        printf("\n  -----\n");
    }
}

int analisar_jogo(char m[3][3]) {
    for (int i = 0; i < 3; i++) {
        if (m[i][0] == m[i][1] && m[i][1] == m[i][2]) {
            if (m[i][0] == 'X') {
                return 1;
            } else if (m[i][0] == 'O') {
                return 2;
            }
        }
    }

    for (int j = 0; j < 3; j++) {
        if (m[0][j] == m[1][j] && m[1][j] == m[2][j]) {
            if (m[0][j] == 'X') {
                return 1;
            } else if (m[0][j] == 'O') {
                return 2;
            }
        }
    }
    if (m[0][0] == m[1][1] && m[1][1] == m[2][2]) {
        if (m[0][0] == 'X') {
            return 1;
        } else if (m[0][0] == 'O') {
            return 2;
        }
    }
    if (m[0][2] == m[1][1] && m[1][1] == m[2][0]) {
        if (m[0][2] == 'X') {
            return 1;
        } else if (m[0][2] == 'O') {
            return 2;
        }
    }

    bool tem_vazia = false;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (m[i][j] == '.') {
                tem_vazia = true;
                break;
            }
        }
        if (tem_vazia) {
            break;
        }
    }
    if (!tem_vazia) {
        return 3;
    }

    return 4;
}

bool jogada_valida(char m[3][3], char jogador, int i, int j) {
    if (i < 0 || i > 2 || j < 0 || j > 2) {
        return false;
    }
    if (m[i][j] != '.') {
        return false;
    }
    return true;
    }
int main() {
    char matriz[3][3] = {{'.', '.', '.'}, {'.', '.', '.'}, {'.', '.', '.'}};
    bool jogada_valida_flag;
    int linha, coluna, jogada_atual = 1;
    char jogador_atual = 'X';
    int status_jogo = 4;

    while (status_jogo == 4) {
        imprimir(matriz);
        printf("Jogador %c, faça sua jogada (linha coluna): ", jogador_atual);
        scanf("%d %d", &linha, &coluna);
        linha--;
        coluna--;

        jogada_valida_flag = jogada_valida(matriz, jogador_atual, linha, coluna);
        if (jogada_valida_flag) {
            matriz[linha][coluna] = jogador_atual;
            status_jogo = analisar_jogo(matriz);
            if (status_jogo == 4) {
                if (jogador_atual == 'X') {
                    jogador_atual = 'O';
                } else {
                    jogador_atual = 'X';
                }
                jogada_atual++;
            }
        } else {
            printf("Jogada inválida. Tente novamente.\n");
        }
    }

    imprimir(matriz);

    if (status_jogo == 1 || status_jogo == 2) {
        printf("O jogador %c ganhou!\n", jogador_atual);
    } else {
        printf("O jogo empatou!\n");
    }

    return 0;
}

