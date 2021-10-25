/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package listasLigadas1358;

import ico.fes.edd1358.LinkedListADT;
import ico.fes.unam.adts.DoubleLinkedList;

/**
 *
 * @author jose
 */
public class ListasLigadas1358 {
    public static void main(String[] args) {
        
        LinkedListADT lst = new LinkedListADT();
        
        lst.append(1);
        lst.append(2);
        lst.append(3);
        lst.append(4);
        lst.preAppend(0);
        lst.transversal();
        
//        DoubleLinkedList ld = new DoubleLinkedList();
//        
//        ld.append(10);
//        ld.append(20);
//        ld.append(30);
//        ld.transversal();
        
    }
}
