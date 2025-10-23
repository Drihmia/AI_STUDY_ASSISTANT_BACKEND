
{ pkgs ? import <nixpkgs> {} }:

let
  google-generativeai = pkgs.python3Packages.buildPythonPackage rec {
    pname = "google-generativeai";
    version = "0.5.4";
    src = pkgs.python3Packages.fetchPypi {
      inherit pname version;
      hash = "sha256-somehash";  # We'll get the correct hash in the next step
    };
    doCheck = false;
    propagatedBuildInputs = with pkgs.python3Packages; [ google-api-core google-auth google-ai-generativelanguage tqdm ];
  };
in
pkgs.mkShell {
  buildInputs = [
    (pkgs.python3.withPackages (ps: with ps; [
      flask
      flask-compress
      flask-cors
      python-dotenv
      beautifulsoup4
      pymongo
      gunicorn
      requests
      gevent
      greenlet
      werkzeug
      google-generativeai
    ]))
  ];
}
