### Nhiệm vụ
    1. Nhập hai số a, b

### Lời giải
    **Đầu tiên**
    - Tôi sẽ sử dụng `disas phase_3` để phân tích mã assembly của hàm `phase_3`.
    - Tiếp theo tôi sẽ quan tâm những phần sau:

    ```asm
       0x000055555555563d <+4>:	sub    $0x18,%rsp
	   0x0000555555555641 <+8>:	mov    %fs:0x28,%rax
	   0x000055555555564a <+17>:	mov    %rax,0x8(%rsp)
	   0x000055555555564f <+22>:	xor    %eax,%eax
	   0x0000555555555651 <+24>:	lea    0x4(%rsp),%rcx
	   0x0000555555555656 <+29>:	mov    %rsp,%rdx
	   0x0000555555555659 <+32>:	lea    0x1caf(%rip),%rsi
    ```
    - Đoạn mã trên chuẩn bị các tham số cho hàm `scanf`. Các giá trị được truyền vào các thanh ghi `%rcx`, `%rdx`, và `%rsi`.
    	-> `x/s $rip + 0x1caf = "%d %d"` cho thấy `scanf` sẽ đọc vào hai số nguyên.

    ```asm
	   0x0000555555555665 <+44>:	cmp    $0x1,%eax
	   0x0000555555555668 <+47>:	jle    0x555555555688 <phase_3+79>
	   0x000055555555566a <+49>:	cmpl   $0x7,(%rsp)
	   0x000055555555566e <+53>:	ja     0x555555555704 <phase_3+203>
    ```
    - `cmp $0x1,%eax` so sánh giá trị trả về của `scanf` (số lượng mục đọc thành công) với 1.
    - `jle 0x555555555688 <phase_3+79>`: Nếu số lượng mục đọc được nhỏ hơn hoặc bằng 1, chương trình sẽ nhảy đến `<phase_3+79>`, ngụ ý người dùng phải nhập >= 2 số.
    - `cmpl $0x7,(%rsp)` so sánh số đầu tiên nhập vào với 7.
    - `ja 0x555555555704 <phase_3+203>`: Nếu số đầu tiên lớn hơn 7, chương trình nhảy đến `<explode_bomb>`, vậy số đầu tiên phải trong khoảng 0-7.

    ```asm
	   0x0000555555555674 <+59>:	mov    (%rsp),%eax
	   0x0000555555555677 <+62>:	lea    0x1b22(%rip),%rdx        # 0x5555555571a0
	   0x000055555555567e <+69>:	movslq (%rdx,%rax,4),%rax
	   0x0000555555555682 <+73>:	add    %rdx,%rax
	   0x0000555555555685 <+76>:	notrack jmp *%rax
    ```
    - Số đầu tiên nhập vào được dùng làm index mảng, chương trình sẽ nhảy đến địa chỉ tương ứng trong mảng.
    - Nếu INPUT là `1 2`, chương trình nhảy đến:

    ```asm
	   0x00005555555556d3 <+154>:	mov    $0x0,%eax
	   0x00005555555556d8 <+159>:	jmp    0x555555555694 <phase_3+91>
    ```
    - Gán `%eax = 0`, sau đó nhảy tới `<phase_3+91>`.
    
    ```asm
       0x0000555555555694 <+91>:	sub    $0x24c,%eax
	   0x0000555555555699 <+96>:	add    $0x2b0,%eax
	   0x000055555555569e <+101>:	sub    $0x7e,%eax
	   0x00005555555556a1 <+104>:	add    $0x7e,%eax
	   0x00005555555556a4 <+107>:	sub    $0x7e,%eax
	   0x00005555555556a7 <+110>:	add    $0x7e,%eax
	   0x00005555555556aa <+113>:	sub    $0x7e,%eax
	   0x00005555555556ad <+116>:	cmpl   $0x5,(%rsp)
	   0x00005555555556b1 <+120>:	jg     0x5555555556b9 <phase_3+128>
	   0x00005555555556b3 <+122>:	cmp    %eax,0x4(%rsp)
	   0x00005555555556b7 <+126>:	je     0x5555555556be <phase_3+133>
	   0x00005555555556b9 <+128>:	call   0x555555555be5 <explode_bomb>
    ```
    - Thực hiện các phép tính trên `%eax` (hiện tại là 0):
    	- `%eax` = 0 - 588 = -588
    	- `%eax` = -588 + 688 = 100
    	- `%eax` = 100 - 126 = -26
    	- `%eax` = -26 + 126 = 100
    	- `%eax` = 100 - 126 = -26
    	- `%eax` = -26 + 126 = 100
    	- `%eax` = 100 - 126 = **-26**
    - Sau đó so sánh `%eax` với số thứ hai nhập vào (`0x4(%rsp)`). Nếu bằng nhau, nhảy đến `<phase_3+133>`. Nếu số thứ hai lớn hơn 5, gọi `<explode_bomb>`.

    ```asm
	   0x00005555555556be <+133>:	mov    0x8(%rsp),%rax
	   0x00005555555556c3 <+138>:	xor    %fs:0x28,%rax
	   0x00005555555556cc <+147>:	jne    0x555555555710 <phase_3+215>
	   0x00005555555556ce <+149>:	add    $0x18,%rsp   
    ```
    - Đoạn này kiểm tra stack canary, nếu không có lỗi thì giải phóng stack và trả về.


**Như vậy: **
Nếu số thứ 1 tôi nhập là 1 thì số thứ 2 phải là -26!