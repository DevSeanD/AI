//Author: Sean Dever
//Date: 3/28/2021
//Description: This application has been created to serve as a learning example of dynamic programming. The problem solved here is the edit distance problem. Two strings will be entered and compared. Using a dynamic programming array the program will determine the minimum amount of edits required to transform string0 into string1.

#include <iostream>
#include <bits/stdc++.h>
#include <vector>
using namespace std;

int minOfVals(int x,int y,int z){
	if(x <= y && x <= z)
		return x;
	if(y <= x && y <= z)
		return y;
	if(z <= x && z <= y)
		return z;
}

int editDistance(string str0,string str1,int m,int n){
	// If the first/second string is empty then the only operations to perform are to add all characters of the other string
	if(m == 0)
		return n;
	if(n == 0)
		return m;
	
	// If the last two characters of the two strings are the same, ignore the last two characters and count remaining chars
	if(str0[m-1] == str1[n-1])
		return editDistance(str0,str1,m-1,n-1);

	// If the last characters are not the same, consider all three operations on the last character of the first string,
	// recursively compute minimum cost for all three
	// operations and take minimum values.A
	
	return 1 + minOfVals(editDistance(str0, str1, m, n - 1), editDistance(str0, str1, m - 1, n), editDistance(str0, str1, m - 1, n - 1));

}

string stringToLower(string str){
	for(int c = 0; c < str.length(); c++){
		str[c] = tolower(str[c]);
	}	
	return str;
}


int main(int argc, char** argv){
	
	int minVal;
	
	// testing the minOfVals function
	// minVal = minOfVals(3,5,10);
	//cout << minVal << endl;
	
	if(argv[1] && argv[2] && argv[3]){
		string word = argv[1];               // choice word
		int distance = atoi(argv[2]);       // distance of edit distance from choice word
		string dictionary = argv[3]; 	   // path to dictionary file
			
		word = stringToLower(word); // convert inputted string to lower case
		std::ifstream file(dictionary); // creating file object with path = dictionary
		std::string str;
		int result;
		int lineNum = 0;
		cout << "Words that were within the target distance:" << endl;
		while (std::getline(file, str)) {
			if(lineNum >= 1){ // skip line 0 
				string str0 = str; // current word to be scanned
				string str1 = word; // choice word to be compared to
				result = editDistance(str0,str1,str0.length(),str1.length());

				if(result <= distance){ // if the number of operations is equal to or less than the specified value.
					cout << str0 << endl;
				}
			}
			lineNum++;
		}
	}	

	return 0;
}
