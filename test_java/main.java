public class main {
    public static void main(String[] args) {
        String[] language={"Python","Java","C","C++","Go","JavaScript","Swift","C#"};
        int count=1;

        System.out.print(count+++". "+language[count-1]+"\n"); // 1. python처럼 +로 구분할 수 있다.

        System.out.println(count+++". "+language[count-1]); // 2. println은 자동적으로 줄 바꿈이 된다.

        System.out.printf("%d. %s",count++,language[count-1]); // 3. C와 같이 printf를 사용할 수 있다.
    }
}