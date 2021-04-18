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
//  	N&n - 4	 | array index - N = 4;  n = 5
//  	R&r - 4	 | array index - R = 6;  r = 7
//  	K&k - 2	 | array index - K = 8;  k = 9
//	Q&q - 2	 | array index - Q = 10; q = 11
//
// Source of values: https://www.chessprogramming.org/Simplified_Evaluation_Function

void updateArr(char currentChar,int bPieceArr[],int wPieceArr[])
{//update array based on the number of each piece in the game state
	switch(int(currentChar)) //ascii code of char
	{
		case 80:
			bPieceArr[0]++;
			break;
		case 112:
			wPieceArr[0]++;
			break;
		case 66:
			bPieceArr[1]++;
			break;
		case 98:
			wPieceArr[1]++;
			break;
		case 78:
			bPieceArr[2]++;
			break;
		case 110:
			wPieceArr[2]++;
			break;
		case 82:
			bPieceArr[3]++;
			break;
		case 114:
			wPieceArr[3]++;
			break;
		case 75:
			bPieceArr[4]++;
			break;
		case 107:
			wPieceArr[4]++;
			break;
		case 81:
			bPieceArr[5]++;
			break;
		case 113:
			wPieceArr[5]++;
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

void readGameState(string gameFileName,int bPieceArr[],int wPieceArr[])
{// returns array containing # of each piece in a given game state file
	fstream gameState;
	//int* bPieceCount = new int[5]; // create a pointer that points to an array of size 5
	//int* wPieceCount = new int[5]; // create a pointer that points to an array of size 5

  gameState.open(gameFileName,ios::in); //open game state file to be read

  if(gameState.is_open()){   //verify game state file is open
		string space;
		char temp;
    while(getline(gameState, space)){ //read game state from file
			cout << space << endl;
			// need to loop through each char in space and compare each to piece id
			for(int c = 0;c <= 7; c++){
				temp = space[c];
				updateArr(temp,bPieceArr,wPieceArr);
			}
  	}
		gameState.close(); //close the file object.
  }
}

float evaluatePieceAdvantage(int* bPieceArr,int* wPieceArr)
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

	for(int c = 0; c <= 5; c++)
	{
		bTotal += bPieceArr[c] * pieceValArr[c];
		wTotal += wPieceArr[c] * pieceValArr[c];
	}

	cout << "White: " << wTotal << endl;
	cout << "Black: " << bTotal << endl;
	return bTotal - wTotal; // returning heuristic
}

int main(int argc, char** argv)
{
	string requestedFile;
	int wPieceNumCount[5]; // white piece count array
	int bPieceNumCount[5]; // black piece count array
	float  pieceResult;

	for(int i = 0; i <= 5; i++) //init each index in the arrays to hold a value of 0
	{
		bPieceNumCount[i] = 0;
		wPieceNumCount[i] = 0;
	}

	if(argv[1])
	{
		requestedFile = argv[1];
		readGameState(requestedFile,bPieceNumCount,wPieceNumCount);
		pieceResult = evaluatePieceAdvantage(bPieceNumCount,wPieceNumCount);
		// purely for read ability for this program. The result returned by evaluation function is a float and NOT a string
		cout << "Black's piece based advantage: " << pieceResult << endl;
	}
	else
	{
		cout << "Incorrect arguments..." << endl;
		cout << "Usage: ./ChessEvaluation.o *CHESS_FILE_NAME*" << endl;
	}
	return 0;
}
