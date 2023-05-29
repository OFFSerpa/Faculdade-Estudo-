#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include <locale.h>

#define WORD_SIZE 5
#define MAX_GUESSES 6
#define DICTIONARY_FILE "palavras.txt"
#define SCORE_FILE "scores.txt"

typedef struct Player {
    char name[50];
    int score;
} Player;


int read_dictionary(char word_list[][WORD_SIZE+1], int max_words) {
    FILE* fp;
    char word[WORD_SIZE+1];
    int i = 0;

    fp = fopen(DICTIONARY_FILE, "r");
    if (fp == NULL) {
        printf("Erro ao abrir o arquivo de dicion�rio.\n");
        return -1;
    }

    while (fgets(word, WORD_SIZE+1, fp) != NULL && i < max_words) {
        word[strcspn(word, "\n")] = 0; 
        if (strlen(word) > WORD_SIZE) {
            continue;
        }
        if (strlen(word) == WORD_SIZE && !strchr(word, ' ')) {
            
            strcpy(word_list[i], word);
            i++;
        }
    }

    fclose(fp);

    return i;
}


void mark_guess(char* word, char* guess, char* result) {
    int i, j;
    for (i = 0; i < WORD_SIZE; i++) {
        if (word[i] == guess[i]) {
            result[i] = '^';
        } else {
            result[i] = 'x';
        }
    }
    for (i = 0; i < WORD_SIZE; i++) {
        if (result[i] == 'x') {
            for (j = 0; j < WORD_SIZE; j++) {
                if (word[i] == guess[j]) {
                    result[j] = '!';
                    break;
                }
            }
        }
    }
    result[WORD_SIZE] = '\0';
}


int choose_word(char word_list[][WORD_SIZE+1], int num_words) {
    int i, valid_words[num_words], valid_count = 0;
    for (i = 0; i < num_words; i++) {
        if (strlen(word_list[i]) >= WORD_SIZE) {
            valid_words[valid_count] = i;
            valid_count++;
        }
    }
    if (valid_count == 0) {
        return -1; 
    }
    srand(time(NULL));
    return valid_words[rand() % valid_count];
}

#include <time.h> 

time_t start_time, end_time; 


void start_timer() {
    time(&start_time);
}

Player get_player_info() {
    Player player;
    printf("Digite seu nome: ");
    scanf("%s", player.name);
    getchar();
    player.score = 0;
    return player;
}


void stop_timer() {
    time(&end_time);
}

int get_elapsed_time() {
    return (int) difftime(end_time, start_time);
}


int main() {
    setlocale(LC_ALL , "portuguese");
	Player player = get_player_info();
	start_timer();
    char word_list[10000][WORD_SIZE+1];
    int num_words, word_index, guess_num, correct_letters, i, j, score = 0;
    char guess[WORD_SIZE+1], result[WORD_SIZE+1], p;
    FILE* score_file;
    num_words = read_dictionary(word_list, 10000);
    if (num_words < 1) {
        return 1;
    }

    word_index = choose_word(word_list, num_words);
    

    printf("Voc� est� jogando o Termo do Toguro!\n");
    for (guess_num = 1; guess_num <= MAX_GUESSES; guess_num++) {
        printf("Tentativa %d de %d. Digite uma palavra de %d letras: ", guess_num, MAX_GUESSES, WORD_SIZE);
        scanf("%s", guess);

        mark_guess(word_list[word_index], guess, result);
        printf("Resultado: %s\n", result);

        if (strcmp(word_list[word_index], guess) == 0) {
            printf("Parabens, voce acertou a palavra \"%s\" em %d tentativas!\n", word_list[word_index], guess_num);
            score += MAX_GUESSES - (guess_num - 1);
            stop_timer();
            break;
        }
    }
	
    if (guess_num > MAX_GUESSES) {
        printf("Que pena, voce nao acertou a palavra \"%s\".\n", word_list[word_index]);
        stop_timer();
    }
    printf("Tempo gasto: %d segundos\n", get_elapsed_time());
    
    score_file = fopen(SCORE_FILE, "a");
	if (score_file != NULL) {
    	fprintf(score_file, "Nome: %s\n%d tentativas\n%d segundos \n\n", player.name, score, get_elapsed_time());
    	fclose(score_file);
	} else {
    printf("Erro ao abrir o arquivo de pontua�es.\n");
}


    
    return 0;
}