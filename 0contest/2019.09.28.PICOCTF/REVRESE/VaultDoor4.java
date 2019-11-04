import java.util.*;

class VaultDoor4 {
    public static void main(String args[]) {
        StringBuilder sb = new StringBuilder();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 062 , 066 ,
            '7' , 'e' , '0' , '3' , 'd' , '1' , '1' , '6' ,
        };
        for (int i=0; i<32; i++) {
            sb.append((char)(myBytes[i]));  
        }
        System.out.println("picoCTF{"+sb.toString()+"}");
    }
}