//go:build tools
// +build tools

package pomerium_console

import (
	_ "github.com/golang/protobuf/protoc-gen-go"                // for generating protobuf
	_ "github.com/pseudomuto/protoc-gen-doc/cmd/protoc-gen-doc" // for generating docs
)
