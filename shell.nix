let
  pkgs = import <nixpkgs> {};
in
pkgs.mkShell {
  packages = with pkgs; [
    nasm
    gdb
    binutils

    python312Full
    python312Packages.numpy
    python312Packages.matplotlib
  ];
}
