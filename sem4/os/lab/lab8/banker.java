import java.util.*;

public class banker {

    static void calcNeeded(int need[][], int maxm[][],int allot[][]){
        for (int i = 0 ; i < maxm.length ; i++)
            for (int j = 0 ; j < maxm[0].length ; j++)
                need[i][j] = maxm[i][j] - allot[i][j];
    }
    
    static boolean isSafe(int processes[], int avail[], int maxm[][],int allot[][]){
        int [][]need = new int[maxm.length][maxm[0].length];
        calcNeeded(need, maxm, allot);
        printMatrix(need, processes, "Need");
        boolean finish[] = new boolean[maxm.length];
        int safeSeq[] = new int[maxm.length];
        int work[] = new int[maxm[0].length];
        for (int i = 0; i < maxm[0].length ; i++)
            work[i] = avail[i];
    
        int count = 0;
        while (count < maxm.length){
            boolean found = false;
            for (int p = 0; p < maxm.length; p++){
                if (finish[p] == false){
                    int j;
                    for (j = 0; j < maxm[0].length; j++)
                        if (need[p][j] > work[j])
                            break;
    
                    if (j == maxm[0].length){
                        for (int k = 0 ; k < maxm[0].length ; k++)
                            work[k] += allot[p][k];
                        safeSeq[count++] = p;
                        finish[p] = true;
                        found = true;
                    }
                }
            }
    
            if (found == false){
                System.out.print("System is not in safe state");
                return false;
            }
        }
    
        System.out.print("System is in safe state.\nSafe sequence is: ");
        for (int i = 0; i < maxm.length ; i++)
            System.out.print("P" + safeSeq[i] + " ");
    
        return true;
    }

    static void printMatrix(int [][] mat,int arr[],String msg){
        System.out.println(msg);
        for(int i = 0;i<mat.length;i++){
            System.out.print("P"+arr[i]+"  ");
            for(int j=0;j<mat[i].length;j++){
                System.out.print(mat[i][j] + "  ");
            }
            System.out.println("");
        }
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int p,r;
        System.out.print("Please enter number of processes:");
        p = in.nextInt();
        System.out.print("Please enter number of types of resources:");
        r = in.nextInt();
        int processes[] = new int[p];
        for(int i=0;i<processes.length;i++) processes[i] = i;
        int avail[] = new int[r];
        for(int i=0;i<avail.length;i++) {
            System.out.print("Please enter number of resources of type " + i + ":");
            avail[i] = in.nextInt();
        }
        int maxm[][] = new int[p][r];
        System.out.println("Please enter values for the Maximum matrix["+p+","+r+"].");
        for(int i = 0;i<maxm.length;i++){
            for(int j=0;j<maxm[i].length;j++){
                maxm[i][j] = in.nextInt();
            }
        }
        int allot[][] = new int[p][r];
        System.out.println("Please enter values for the Alloted matrix["+p+","+r+"].");
        for(int i = 0;i<allot.length;i++){
            for(int j=0;j<allot[i].length;j++){
                allot[i][j] = in.nextInt();
            }
        } 
        System.out.println("  ");
        printMatrix(maxm,processes,"Maximum");
        printMatrix(allot,processes,"Allocated");
        isSafe(processes, avail, maxm, allot);
        System.out.println("");
        in.close();
    }
}
