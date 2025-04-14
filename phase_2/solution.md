### Nhiệm vụ
    1. Nhập hai số a, b

### Lời giải
    **Đầu tiên**
    - Tôi sẽ sử dụng *disas phase_3*
    - Tiếp theo tôi sẽ quan tâm những phần sau:

    ```asm
       0x000055555555563d <+4>:	sub    $0x18,%rsp
	   0x0000555555555641 <+8>:	mov    %fs:0x28,%rax
	   0x000055555555564a <+17>:	mov    %rax,0x8(%rsp)
	   0x000055555555564f <+22>:	xor    %eax,%eax
	   0x0000555555555651 <+24>:	lea    0x4(%rsp),%rcx
	   0x0000555555555656 <+29>:	mov    %rsp,%rdx
	   0x0000555555555659 <+32>:	lea    0x1caf(%rip),%rsi
    ```
    - Tôi thấy ở đây đang truyền tham số vào các thanh ghi để thực hiện `scanf`
    	-> `x/s $rip + 0x1caf = "%d %d"`

    ```asm
	   0x0000555555555665 <+44>:	cmp    $0x1,%eax
	   0x0000555555555668 <+47>:	jle    0x555555555688 <phase_3+79>
	   0x000055555555566a <+49>:	cmpl   $0x7,(%rsp)
	   0x000055555555566e <+53>:	ja     0x555555555704 <phase_3+203>
    ```