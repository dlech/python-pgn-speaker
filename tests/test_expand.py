# SPDX-License-Identifier: MIT
# Copyright (c) 2023 David Lechner <david@lechnology.com>

from pgn_speaker.cli import expand


def test_basic():
    assert expand("e5") == "e5"
    assert expand("Bc4") == "bishop c4"


def test_captures():
    assert expand("exd5") == "e takes d5"
    assert expand("Bxf7") == "bishop takes f7"
    assert expand("Rxa8+") == "rook takes a8 check"


def test_disambiguation():
    assert expand("Nfd2") == "knight f d2"
    assert expand("Qh4xg3#") == "queen h4 takes g3 checkmate"


def test_castling():
    assert expand("O-O") == "castles kingside"
    assert expand("O-O-O") == "castles queenside"
    assert expand("O-O+") == "castles kingside check"
    assert expand("O-O-O+") == "castles queenside check"
    assert expand("O-O#") == "castles kingside checkmate"
    assert expand("O-O-O#") == "castles queenside checkmate"


def test_promotion():
    assert expand("e8=Q") == "e8 promotes to queen"
    assert expand("exd1=N#") == "e takes d1 promotes to knight checkmate"
