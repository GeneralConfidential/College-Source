import java.util.*;
public class mlth {
	static mlth m = new mlth();
    static synchronized void table(int n) {
		for(int i=1;i<11;i++) {
			System.out.println(n+" x " + i + " = " + n*i);
		}
        System.out.println();
	}
	public class T1 extends Thread{
		public void run(){
			table(5);
		}
	}
	public class T2 extends Thread{
		public void run(){
			table(6);
		}
	}
	public static void main(String[] args) {
		T1 t1 = m.new T1();
		T2 t2 = m.new T2();
		t1.start();
		t2.start();
	}
}
