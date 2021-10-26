/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ico.fes.edd1358;

/**
 *
 * @author jose
 */
public class LinkedListADT {

    private class Nodo<T> {

        T data;
        Nodo next;

        public Nodo(T valor) {
            this.data = valor;
        }

        public Nodo(T valor, Nodo siguiente) {
            this.data = valor;
            this.next = siguiente;
        }
    }

    private Nodo head;

    public LinkedListADT() {
        this.head = null;
    }

    public boolean isEmpty() {
        return this.head == null;
    }

    private Nodo getTail() {
        Nodo currNode = this.head;
        if ( !this.isEmpty() ) {
            while (currNode.next != null) {
                currNode = currNode.next;
            }
        }
        return currNode;
    }

    public void append(Object valor) {
        if (this.isEmpty()) {
            this.head = new Nodo(valor);
        } else {
            this.getTail().next = new Nodo(valor);
        }
    }
    
    public void preAppend( Object valor ){
        Nodo tmp = this.head;
        this.head = new Nodo( valor, tmp );
    }

    public void transversal() {

        Nodo currNode = this.head;
        while (currNode != null) {
            if (currNode.next == null) {
                System.out.print(currNode.data);
            } else {
                System.out.print(currNode.data + " ---> ");
            }
//            System.out.println(currNode.data);
            currNode = currNode.next;
        }
        System.out.println("");
    }

    public void remove(){
        
    }
    
}
