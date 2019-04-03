
#include <stdio.h>  
  
#include <iostream>  
#include <fstream>  
#include <sstream>  
  
#include <cryptopp/aes.h>  
#include <cryptopp/filters.h>  
#include <cryptopp/modes.h>  
  
using namespace std;
#define byte uint8_t

byte key[ CryptoPP::AES::DEFAULT_KEYLENGTH ], iv[ CryptoPP::AES::BLOCKSIZE];  
  
void initKV()  
{  
    memset( key, 0x00, CryptoPP::AES::DEFAULT_KEYLENGTH );  
    memset( iv, 0x00, CryptoPP::AES::BLOCKSIZE );  
}  
  
string encrypt(string plainText)  
{  
    string cipherText;  
  
    //  
    CryptoPP::AES::Encryption aesEncryption(key, CryptoPP::AES::DEFAULT_KEYLENGTH);  
    CryptoPP::CBC_Mode_ExternalCipher::Encryption cbcEncryption( aesEncryption, iv );  
    CryptoPP::StreamTransformationFilter stfEncryptor(cbcEncryption, new CryptoPP::StringSink( cipherText ));  
    stfEncryptor.Put( reinterpret_cast<const unsigned char*>( plainText.c_str() ), plainText.length() + 1 );  
    stfEncryptor.MessageEnd();  
  
    string cipherTextHex;  
    for( int i = 0; i < cipherText.size(); i++ )  
    {  
        char ch[3] = {0};  
        sprintf(ch, "%02x",  static_cast<byte>(cipherText[i]));  
        cipherTextHex += ch;  
    }  
  
    return cipherTextHex;  
}  
  
  
  
void writeCipher(string output)  
{  
    ofstream out("/tmp/cipher.data");  
    out.write(output.c_str(), output.length());  
    out.close();  
  
    cout<<"writeCipher finish "<<endl<<endl;  
}  
  
  
  
int main()  
{  
    string text;
    getline(cin,text); 
    cout<<"text : "<<text<<endl;  
  
    initKV();  
    string cipherHex = encrypt(text);  
    cout<<"cipher : "<<cipherHex<<endl;  
    writeCipher(cipherHex);  
  
    return 0;  
}  