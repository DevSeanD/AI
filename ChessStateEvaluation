#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// Author: Sean Dever
// Data: 4/7/21
// Description - Chess Game State Evalutation Program -- This program will evaluate which player, black or white,
//								is winning any given game based on its current state.
//
// Black will be denoted in uppercase
// While will be denoted in lowercase
//
// Total number of each piece and corresponding array indices:
// 	P&p - 16 | array index - P = 0;  p = 1
//	B&b - 4  | array index - B = 2;  b = 3
//  N&n - 4	 | array index - N = 4;  n = 5
//  R&r - 4	 | array index - R = 6;  r = 7
//  K&k - 2	 | array index - K = 8;  k = 9
//	Q&q - 2	 | array index - Q = 10; q = 11
//
// Source of values: https://www.chessprogramming.org/Simplified_Evaluation_Function

void updateArr(char currentChar,int pieceArr[])
{//update array based on the number of each piece in the game state
	switch(int(currentChar)) //ascii code of char
	{
		case 80:
			pieceArr[0]++;
			break;
		case 112:
			pieceArr[1]++;
			break;
		case 66:
			pieceArr[2]++;
			break;
		case 98:
			pieceArr[3]++;
			break;
		case 78:
			pieceArr[4]++;
			break;
		case 110:
			pieceArr[5]++;
			break;
		case 82:
			pieceArr[6]++;
			break;
		case 114:
			pieceArr[7]++;
			break;
		case 75:
			pieceArr[8]++;
			break;
		case 107:
			pieceArr[9]++;
			break;
		case 81:
			pieceArr[10]++;
			break;
		case 113:
			pieceArr[11]++;
			break;
	}
}

void displayCountState(int* gameStateArr)
{// ouput to console the contents of gameStateArr
	for(int c = 0; c <= 11; c++)
	{
		cout << gameStateArr[c] << "\t";
	}
}

int* readGameState(string gameFileName)
{// returns array containing # of each piece in a given file
	fstream gameState;
	int* pieceCount = new int[11]; // create a pointer that points to an array of size 11

	for(int i = 0; i <= 11; i++) //init each index in the array to hold a value of 0
	{
		pieceCount[i] = 0;
	}
  gameState.open(gameFileName,ios::in); //open game state file to be read

  if(gameState.is_open()){   //verify game state file is open
		string space;
		char temp;
    while(getline(gameState, space)){ //read game state from file
			// need to loop through each char in space and compare each to piece id
			for(int c = 0;c <= 7; c++){
				temp = space[c];
				updateArr(temp,pieceCount);
			}
  	}
		gameState.close(); //close the file object.
  }
	return pieceCount; // return the array pointer
}

string evaluatePieceAdvantage(int* pieceCountArr)
{// decide which player has the advantage based on pieces
	int bTotal = 0; // black total
	int wTotal = 0;	// white Total
	int pieceValArr[5]; // value of each piece type
	int valCount = 0;

	pieceValArr[0] = 100; // pawns
	pieceValArr[1] = 330; // bishops
	pieceValArr[2] = 320; // knights
	pieceValArr[3] = 500; // rooks
	pieceValArr[4] = 20000; // kings
	pieceValArr[5] = 900; // queens

	for(int c = 0; c <= 11; c++)
	{
		bTotal += pieceCountArr[c] * pieceValArr[valCount];
		c++;
		wTotal += pieceCountArr[c] * pieceValArr[valCount];
		valCount++;
	}

	if(bTotal > wTotal)
	{
		return "Black has the piece based advantage";
	}
	if(wTotal > bTotal)
	{
		return "White has the piece based advantage";
	}
	if(wTotal == bTotal)
	{
		return "Neither player has an advantage";
	}
	else
	{
		return "Evaluation function failed";
	}
}


int main(int argc, char** argv)
{
	string requestedFile;
	int* pieceNumCount;
	string pieceResult;
	if(argv[1])
	{
		requestedFile = argv[1];
		pieceNumCount = readGameState(requestedFile);

		pieceResult = evaluatePieceAdvantage(pieceNumCount);
		cout << pieceResult << endl;
	}
	else
	{
		cout << "Incorrect arguments..." << endl;
		cout << "Ex: ./ChessEvaluation.o *CHESS_FILE_NAME*" << endl;
	}
	return 0;
}
