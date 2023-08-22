public class Deque1
{
    private int[] deque;
    private int length;
    private int starts;
    public Deque1()
    {
        // array size changed to double of its original size (1_000_000)
        deque = new int[2_000_000];
        length = 0;
        starts = 1_000_000; // starts in 1_000_000, we don't have to use move function
    }
    public void f1(int n)
    {
        deque[--starts] = n;
        length++;
    }
    /*private void move() // Time exceeded while using this
    {
        if(length >= 1) 
        {
            for(int i = length-1; i >= starts; i--) deque[i + 1] = deque[i];
        }
    }
    */
    public void f2(int n)
    {
        deque[starts + length] = n;
        length++;
    }
    public int f3()
    {
        if(length == 0) return -1;
        else
        {
            length--;
            return deque[starts++];
        }
    }
    public int f4()
    {
        if(length == 0) return -1;
        else
        {
            length--;
            return deque[starts + length];
        }
    }
    public int f5() { return length; }
    public int f6()
    {
        if(length == 0) return 1;
        else return 0;
    }
    public int f7()
    {
        if(length == 0) return -1;
        else return deque[starts];
    }
    public int f8()
    {
        if(length == 0) return -1;
        else return deque[starts + length - 1];
    }
}