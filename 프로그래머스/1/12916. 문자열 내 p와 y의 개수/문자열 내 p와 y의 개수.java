// class Solution {
//     boolean solution(String s) {
//         int p = 0;
//         int y = 0;
        
//         for (int i = 0; i < s.length(); i++) {
//             if (s.charAt(i) == 'p' || s.charAt(i) == 'P') {
//                 p++;
//             }
//             else if (s.charAt(i) == 'y' || s.charAt(i) == 'Y') { 
//                 y++;
//             }
//         }
//         return p == y;
//     }
// }

// class Solution {
//     boolean solution(String s) {
//         int p = 0;
//         int y = 0;
        
//         String lowerS = s.toLowerCase();
//         for (int i = 0; i < lowerS.length(); i++) {
//             if (lowerS.charAt(i) == 'p') {
//                 p++;
//             } else if (lowerS.charAt(i) == 'y') { 
//                 y++;
//             }
//         }
//         return p == y;
//     }
// }

import java.util.stream.Collectors;

class Solution {
    boolean solution(String s) {
        long p = s.chars()
                  .filter(ch -> ch == 'p' || ch == 'P')
                  .count();
        long y = s.chars()
                  .filter(ch -> ch == 'y' || ch == 'Y')
                  .count();
        return p == y;
    }
}