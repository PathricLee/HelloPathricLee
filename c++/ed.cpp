#include <iostream>
#include <vector>
/*
* 计算a->b的编辑距离
* dist[i][j]表示长度为i的字符串变为长度为j的字符串需要的编辑距离
* operation[i][j]表示变换过程中对应的操作
* 0:正确;1:字符替换;2:插入;3:删除
*/
void backtrace(const std::vector<std::vector<uint8_t> > &operation, const char* a, const char* b);

int edit_distance(const char* a, const char* b)
{
    int len_a=strlen(a);
    int len_b=strlen(b);
    std::vector<std::vector<uint8_t> > dist(len_a + 1);
    std::vector<std::vector<uint8_t> > operation(len_a + 1);
    for (int i = 0; i < dist.size(); i++) {
        (dist[i]).resize(len_b + 1);
        (operation[i]).resize(len_b + 1);
    }

    //b为空字符串，将a变为b需要不停地删除a的字符
    for (int i=0;i<=len_a;i++)
    {
        dist[i][0]=i;
        operation[i][0]=3;
    }

    //a为空字符串，将a变为b需要不停地添加b的字符
    for (int j=0;j<=len_b;j++)
    {
        dist[0][j]=j;
        operation[0][j]=2;
    }

    operation[0][0]=0;

    for (int i=1;i<=len_a;i++)
    {
        for (int j=1;j<=len_b;j++)
        {
            uint8_t cost = (a[i-1] == b[j-1] ? 0 : 1);   

            uint8_t deletion = dist[i-1][j] + 1;   
            uint8_t insertion = dist[i][j-1] + 1;   
            uint8_t substitution = dist[i-1][j-1] + cost;   
            uint8_t replace = len_b;

            if (i > 1 && j> 1 && a[i-1] == b[j-2] && a[i-2] == b[j-1]) {
                replace = dist[i-2][j-2] + 1; 
            }

            //如果不回溯直接利用下面这句
            //dist[i][j] = MIN(deletion,MIN(insertion,substitution)); 
            dist[i][j] = std::min(std::min(std::min(deletion, insertion), substitution), replace);
            if (dist[i][j] == substitution) {
                operation[i][j]=cost;
            }
            else if (dist[i][j] == deletion) {
                operation[i][j]=3;
            }
            else if (dist[i][j] == insertion) {
                operation[i][j]=2;
            }
            else if (dist[i][j] == replace) {
                operation[i][j]=4;
            }
        }
    }
    int min = len_a;
    int predict_len = 0;
    int min_index = 0;
    for (int j = len_b; j >= 1; j--) {
        if (dist[len_a][j] < min) {
            min = dist[len_a][j];
            min_index = j;
        }
    }
    printf("predict_len:%d\n", len_b - min_index);
    std::string tmp(b);
    tmp = tmp.substr(0, min_index);
    backtrace(operation, a, tmp.c_str());

    //return dist[len_a][len_b];
    return min;
}

void backtrace(const std::vector<std::vector<uint8_t> > &operation, const char* a, const char* b)
{
    int insertion=0,deletion=0,substitution=0,replace=0;
    int i,j;
    int len1=strlen(a);
    int len2=strlen(b);

    for (i=len1,j=len2;i>=0&&j>=0;)
    {
        switch(operation[i][j])
        {
        case 0:
            //printf("(%d,%d) right\n",i,j);
            printf("pos %d right\n",i);
            i--;
            j--;
            continue;
        case 1:
            //printf("(%d,%d) substitute\n",i,j);
            printf("pos %d substitute (%c-->%c)\n",i,a[i-1],b[j-1]);
            i--;
            j--;
            substitution++;
            continue;
        case 2:
            //printf("(%d,%d) insert\n",i,j);
            printf("pos %d insert (%c)\n",i,b[j-1]);

            j--;
            insertion++;
            continue;
        case 3:
            //printf("(%d,%d) delete\n",i,j);
            printf("pos %d delete (%c)\n",i,a[i-1]);
            i--;
            deletion++;
            continue;
        case 4:
            //printf("(%d,%d) delete\n",i,j);
            printf("pos %d replace (%c) and (%c)\n",i,a[i-1], a[i-2]);
            i -= 2;
            j -= 2;
            replace++;
            continue;
        }
    }

    printf("insert:%d,delete:%d,substitute:%d,replace:%d\n",insertion,deletion,substitution,replace);
}

int main() {
    while (true) {
        std::string a, b;
        std::cin >> a >> b;
        std::cout << edit_distance(a.c_str(), b.c_str()) << std::endl;
    }
    return 0;
}
