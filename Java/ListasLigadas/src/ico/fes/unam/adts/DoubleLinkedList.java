/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ico.fes.unam.adts;

/**
 *
 * @author jose
 */
public class DoubleLinkedList {

    private class NodoDoble<T> {

        T data;
        NodoDoble next;
        NodoDoble prev;

        public NodoDoble() {
        }

        public NodoDoble(T data, NodoDoble next, NodoDoble prev) {
            this.data = data;
            this.next = next;
            this.prev = prev;
        }
    }

    private NodoDoble head;
    private NodoDoble tail;
    private int size;

    public DoubleLinkedList() {
        head = null;
        tail = null;
        this.size = 0;
    }

    public boolean siEmpty() {
        return this.head == null;
    }

    public void append(Object valor) {
        if (this.tail == null) {
            this.tail = new NodoDoble(valor, null, null);
            this.head = this.tail;
        } else {
            this.tail.next = new NodoDoble(valor, null, this.tail);
            this.tail = this.tail.next;
        }
        this.size++;
    }

    public void transversal() {
        NodoDoble currNode = this.head;
        while (currNode != null) {
            if (currNode.next == null) {
                System.out.print(currNode.data);
            } else {
                System.out.print(currNode.data + " ---> ");
            }
            currNode = currNode.next;
        }
        System.out.println("");
    }

    public void reverseTransversal() {
        NodoDoble currNode = this.tail;
        while (currNode != null) {
            if (currNode.prev == null) {
                System.out.print(currNode.data);
            } else {
                System.out.print(currNode.data + " ---> ");
            }
            currNode = currNode.prev;
        }
        System.out.println("");
    }

    public void removeFromHead(Object valor) {
        NodoDoble currNode = this.head;
        if (currNode.data == valor) {
//            System.out.println("1");
            this.head = currNode.next;
            this.head.prev = null;
        } else if (this.tail.data == valor) {
//            System.out.println("2");
            this.tail = this.tail.prev;
            this.tail.next = null;
        } else {
            while (currNode != null) {
                if (currNode.data == valor) {
                    NodoDoble nodoAnt = currNode.prev;
                    NodoDoble nodoSig = currNode.next;

                    nodoAnt.next = nodoSig;
                    nodoSig.prev = nodoAnt;
                    break;
                }
                currNode = currNode.next;
            }
        }
        this.size--;
    }

    public void removeFromTail(Object valor) {
        NodoDoble currNode = this.tail;
        if (currNode.data == valor) {
//            System.out.println("1");
            this.tail = this.tail.prev;
            this.tail.next = null;
        } else if (this.head.data == valor) {
//              System.out.println("2");
            this.head = this.head.next;
            this.head.prev = null;
        } else {
            while (currNode != null) {
                if (currNode.data == valor) {
                    NodoDoble nodoAnt = currNode.prev;
                    NodoDoble nodoSig = currNode.next;

                    nodoAnt.next = nodoSig;
                    nodoSig.prev = nodoAnt;
                    break;
                }
                currNode = currNode.prev;
            }
        }
        this.size--;
    }
    
    public NodoDoble findFromHead( Object valor ){
       NodoDoble currNode = this.head;
        if (currNode.data == valor) {
//            System.out.println("1");
            this.head = currNode.next;
            this.head.prev = null;
        } else if (this.tail.data == valor) {
//            System.out.println("2");
            this.tail = this.tail.prev;
            this.tail.next = null;
            return this.tail;
        } else {
            while (currNode != null) {
                if (currNode.data == valor) {
                    NodoDoble nodoAnt = currNode.prev;
                    NodoDoble nodoSig = currNode.next;

                    nodoAnt.next = nodoSig;
                    nodoSig.prev = nodoAnt;
                    break;
                }
                currNode = currNode.next;
            }
        }
        return currNode;
    }

//    public void head() {
//        System.out.println(this.head.prev);
//    }
//
//    public void tail() {
//        System.out.println(this.tail.data);
//    }
    public int getSize() {
        return size;
    }

}
