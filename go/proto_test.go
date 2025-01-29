package go_test

import (
	"testing"

	"github.com/pomerium/enterprise-client/go/pb"
)

// TestProto tests the proto package can be imported.
func TestProto(*testing.T) {
	_ = pb.Settings{}
}
