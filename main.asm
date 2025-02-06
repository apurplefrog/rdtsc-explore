global _start

section .text

_start:
  rdtsc
  shl rdx, 32
  or rax, rdx

  mov rdx, 0
  mov rax, rax
  mov rbx, 10
  div rbx

  mov rdi, rdx 
  mov rax, 60
  syscall
