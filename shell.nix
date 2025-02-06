let
  pkgs = import <nixpkgs> {};
in
pkgs.mkShell {
  packages = with pkgs; [
    nasm
    nasmfmt
    gdb

    python312Packages.numpy
    python312Packages.matplotlib
  ];
}
