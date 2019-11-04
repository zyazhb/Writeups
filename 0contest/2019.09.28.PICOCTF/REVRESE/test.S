include user32.inc
includelib User32.lib
.code
Winmain Proc
	call asm1
	
	mov bx,[01b4H]
	
	mov ah,4ch
	int 21h
	
Winmain endp

asm1:
	push   ebp
	mov    ebp,esp
	cmp    DWORD PTR [ebp+0x8],0x421
	jg     0x512
	cmp    DWORD PTR [ebp+0x8],0x1b4
	jne    0x50a
	mov    eax,DWORD PTR [ebp+0x8]
	add    eax,0x13
	jmp    0x529
	mov    eax,DWORD PTR [ebp+0x8]
	sub    eax,0x13
	jmp    0x529
	cmp    DWORD PTR [ebp+0x8],0x7f7
	jne    0x523
	mov    eax,DWORD PTR [ebp+0x8]
	sub    eax,0x13
	jmp    0x529
	mov    eax,DWORD PTR [ebp+0x8]
	add    eax,0x13
	pop    ebp
	ret  
asm1 endp
end

;asm1:
;	<+0>:	push   ebp
;	<+1>:	mov    ebp,esp
;	<+3>:	cmp    DWORD PTR [ebp+0x8],0x421
;	<+10>:	jg     0x512 <asm1+37>
;	<+12>:	cmp    DWORD PTR [ebp+0x8],0x1b4
;	<+19>:	jne    0x50a <asm1+29>
;	<+21>:	mov    eax,DWORD PTR [ebp+0x8]
;	<+24>:	add    eax,0x13
;	<+27>:	jmp    0x529 <asm1+60>
;	<+29>:	mov    eax,DWORD PTR [ebp+0x8]
;	<+32>:	sub    eax,0x13
;	<+35>:	jmp    0x529 <asm1+60>
;	<+37>:	cmp    DWORD PTR [ebp+0x8],0x7f7
;	<+44>:	jne    0x523 <asm1+54>
;	<+46>:	mov    eax,DWORD PTR [ebp+0x8]
;	<+49>:	sub    eax,0x13
;	<+52>:	jmp    0x529 <asm1+60>
;	<+54>:	mov    eax,DWORD PTR [ebp+0x8]
;	<+57>:	add    eax,0x13
;	<+60>:	pop    ebp
;	<+61>:	ret    


