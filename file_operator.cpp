#include <iostream>
#include <vector>
#include <sstream>

void lprint(std::vector<std::string> &words);

void read2pipe() {
    // std::in

    std::string line;
    while(std::getline(std::cin, line)) {
        std::istringstream s(line);
        std::string word;
        std::vector<std::string> words;
        while(s >> word) {
            std::string::iterator siter = word.begin();
            bool english = true;
            for(; siter != word.end(); siter++) {
                if (*siter >= 'a' and *siter <= 'z') {
                    
                }
                else if (*siter >= 'A' and *siter <= 'Z') {
                
                }
                else {
                    english = false; 
                }
            }
            if (english) {
                words.push_back(word);
            }
        }
        if (words.size() == 2) {
            lprint(words);
        }
        words.clear();
    }
}

void lprint(std::vector<std::string> &words) {
    for (std::vector<std::string>::iterator iter = words.begin();
            iter != words.end(); iter++) {
        std::cout << (*iter) << "\t";
    }
    std::cout << std::endl;
}

int main() {
    read2pipe();
    return 0;
}
