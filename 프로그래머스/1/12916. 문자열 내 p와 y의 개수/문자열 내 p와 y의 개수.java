class Solution {
    boolean solution(String s) {
        int answer = 0;
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'p' || s.charAt(i) == 'P') {
                answer++;
            }
            else if (s.charAt(i) == 'y' || s.charAt(i) == 'Y') { 
                answer--;
            }
        }
        return answer == 0;
    }
}

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