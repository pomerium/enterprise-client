// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.23.0
// 	protoc        v3.19.4
// source: console_config.proto

package pb

import (
	proto "github.com/golang/protobuf/proto"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// This is a compile-time assertion that a sufficiently up-to-date version
// of the legacy proto package is being used.
const _ = proto.ProtoPackageIsVersion4

type ConsoleConfig struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	KeyPairs   []*KeyPair   `protobuf:"bytes,1,rep,name=key_pairs,json=keyPairs,proto3" json:"key_pairs,omitempty"`
	Namespaces []*Namespace `protobuf:"bytes,2,rep,name=namespaces,proto3" json:"namespaces,omitempty"`
	Policies   []*Policy    `protobuf:"bytes,3,rep,name=policies,proto3" json:"policies,omitempty"`
	Routes     []*Route     `protobuf:"bytes,4,rep,name=routes,proto3" json:"routes,omitempty"`
	Settings   *Settings    `protobuf:"bytes,5,opt,name=settings,proto3" json:"settings,omitempty"`
}

func (x *ConsoleConfig) Reset() {
	*x = ConsoleConfig{}
	if protoimpl.UnsafeEnabled {
		mi := &file_console_config_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ConsoleConfig) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ConsoleConfig) ProtoMessage() {}

func (x *ConsoleConfig) ProtoReflect() protoreflect.Message {
	mi := &file_console_config_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ConsoleConfig.ProtoReflect.Descriptor instead.
func (*ConsoleConfig) Descriptor() ([]byte, []int) {
	return file_console_config_proto_rawDescGZIP(), []int{0}
}

func (x *ConsoleConfig) GetKeyPairs() []*KeyPair {
	if x != nil {
		return x.KeyPairs
	}
	return nil
}

func (x *ConsoleConfig) GetNamespaces() []*Namespace {
	if x != nil {
		return x.Namespaces
	}
	return nil
}

func (x *ConsoleConfig) GetPolicies() []*Policy {
	if x != nil {
		return x.Policies
	}
	return nil
}

func (x *ConsoleConfig) GetRoutes() []*Route {
	if x != nil {
		return x.Routes
	}
	return nil
}

func (x *ConsoleConfig) GetSettings() *Settings {
	if x != nil {
		return x.Settings
	}
	return nil
}

var File_console_config_proto protoreflect.FileDescriptor

var file_console_config_proto_rawDesc = []byte{
	0x0a, 0x14, 0x63, 0x6f, 0x6e, 0x73, 0x6f, 0x6c, 0x65, 0x5f, 0x63, 0x6f, 0x6e, 0x66, 0x69, 0x67,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x12, 0x70, 0x6f, 0x6d, 0x65, 0x72, 0x69, 0x75, 0x6d,
	0x2e, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x1a, 0x0f, 0x6b, 0x65, 0x79, 0x5f,
	0x63, 0x68, 0x61, 0x69, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x10, 0x6e, 0x61, 0x6d,
	0x65, 0x73, 0x70, 0x61, 0x63, 0x65, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x0c, 0x70,
	0x6f, 0x6c, 0x69, 0x63, 0x79, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x0c, 0x72, 0x6f, 0x75,
	0x74, 0x65, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x0e, 0x73, 0x65, 0x74, 0x74, 0x69,
	0x6e, 0x67, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xad, 0x02, 0x0a, 0x0d, 0x43, 0x6f,
	0x6e, 0x73, 0x6f, 0x6c, 0x65, 0x43, 0x6f, 0x6e, 0x66, 0x69, 0x67, 0x12, 0x38, 0x0a, 0x09, 0x6b,
	0x65, 0x79, 0x5f, 0x70, 0x61, 0x69, 0x72, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x1b,
	0x2e, 0x70, 0x6f, 0x6d, 0x65, 0x72, 0x69, 0x75, 0x6d, 0x2e, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f,
	0x61, 0x72, 0x64, 0x2e, 0x4b, 0x65, 0x79, 0x50, 0x61, 0x69, 0x72, 0x52, 0x08, 0x6b, 0x65, 0x79,
	0x50, 0x61, 0x69, 0x72, 0x73, 0x12, 0x3d, 0x0a, 0x0a, 0x6e, 0x61, 0x6d, 0x65, 0x73, 0x70, 0x61,
	0x63, 0x65, 0x73, 0x18, 0x02, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x1d, 0x2e, 0x70, 0x6f, 0x6d, 0x65,
	0x72, 0x69, 0x75, 0x6d, 0x2e, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x2e, 0x4e,
	0x61, 0x6d, 0x65, 0x73, 0x70, 0x61, 0x63, 0x65, 0x52, 0x0a, 0x6e, 0x61, 0x6d, 0x65, 0x73, 0x70,
	0x61, 0x63, 0x65, 0x73, 0x12, 0x36, 0x0a, 0x08, 0x70, 0x6f, 0x6c, 0x69, 0x63, 0x69, 0x65, 0x73,
	0x18, 0x03, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x70, 0x6f, 0x6d, 0x65, 0x72, 0x69, 0x75,
	0x6d, 0x2e, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x2e, 0x50, 0x6f, 0x6c, 0x69,
	0x63, 0x79, 0x52, 0x08, 0x70, 0x6f, 0x6c, 0x69, 0x63, 0x69, 0x65, 0x73, 0x12, 0x31, 0x0a, 0x06,
	0x72, 0x6f, 0x75, 0x74, 0x65, 0x73, 0x18, 0x04, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x19, 0x2e, 0x70,
	0x6f, 0x6d, 0x65, 0x72, 0x69, 0x75, 0x6d, 0x2e, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72,
	0x64, 0x2e, 0x52, 0x6f, 0x75, 0x74, 0x65, 0x52, 0x06, 0x72, 0x6f, 0x75, 0x74, 0x65, 0x73, 0x12,
	0x38, 0x0a, 0x08, 0x73, 0x65, 0x74, 0x74, 0x69, 0x6e, 0x67, 0x73, 0x18, 0x05, 0x20, 0x01, 0x28,
	0x0b, 0x32, 0x1c, 0x2e, 0x70, 0x6f, 0x6d, 0x65, 0x72, 0x69, 0x75, 0x6d, 0x2e, 0x64, 0x61, 0x73,
	0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x2e, 0x53, 0x65, 0x74, 0x74, 0x69, 0x6e, 0x67, 0x73, 0x52,
	0x08, 0x73, 0x65, 0x74, 0x74, 0x69, 0x6e, 0x67, 0x73, 0x42, 0x2d, 0x5a, 0x2b, 0x67, 0x69, 0x74,
	0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x70, 0x6f, 0x6d, 0x65, 0x72, 0x69, 0x75, 0x6d,
	0x2f, 0x70, 0x6f, 0x6d, 0x65, 0x72, 0x69, 0x75, 0x6d, 0x2d, 0x63, 0x6f, 0x6e, 0x73, 0x6f, 0x6c,
	0x65, 0x2f, 0x70, 0x6b, 0x67, 0x2f, 0x70, 0x62, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_console_config_proto_rawDescOnce sync.Once
	file_console_config_proto_rawDescData = file_console_config_proto_rawDesc
)

func file_console_config_proto_rawDescGZIP() []byte {
	file_console_config_proto_rawDescOnce.Do(func() {
		file_console_config_proto_rawDescData = protoimpl.X.CompressGZIP(file_console_config_proto_rawDescData)
	})
	return file_console_config_proto_rawDescData
}

var file_console_config_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_console_config_proto_goTypes = []interface{}{
	(*ConsoleConfig)(nil), // 0: pomerium.dashboard.ConsoleConfig
	(*KeyPair)(nil),       // 1: pomerium.dashboard.KeyPair
	(*Namespace)(nil),     // 2: pomerium.dashboard.Namespace
	(*Policy)(nil),        // 3: pomerium.dashboard.Policy
	(*Route)(nil),         // 4: pomerium.dashboard.Route
	(*Settings)(nil),      // 5: pomerium.dashboard.Settings
}
var file_console_config_proto_depIdxs = []int32{
	1, // 0: pomerium.dashboard.ConsoleConfig.key_pairs:type_name -> pomerium.dashboard.KeyPair
	2, // 1: pomerium.dashboard.ConsoleConfig.namespaces:type_name -> pomerium.dashboard.Namespace
	3, // 2: pomerium.dashboard.ConsoleConfig.policies:type_name -> pomerium.dashboard.Policy
	4, // 3: pomerium.dashboard.ConsoleConfig.routes:type_name -> pomerium.dashboard.Route
	5, // 4: pomerium.dashboard.ConsoleConfig.settings:type_name -> pomerium.dashboard.Settings
	5, // [5:5] is the sub-list for method output_type
	5, // [5:5] is the sub-list for method input_type
	5, // [5:5] is the sub-list for extension type_name
	5, // [5:5] is the sub-list for extension extendee
	0, // [0:5] is the sub-list for field type_name
}

func init() { file_console_config_proto_init() }
func file_console_config_proto_init() {
	if File_console_config_proto != nil {
		return
	}
	file_key_chain_proto_init()
	file_namespaces_proto_init()
	file_policy_proto_init()
	file_routes_proto_init()
	file_settings_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_console_config_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ConsoleConfig); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_console_config_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_console_config_proto_goTypes,
		DependencyIndexes: file_console_config_proto_depIdxs,
		MessageInfos:      file_console_config_proto_msgTypes,
	}.Build()
	File_console_config_proto = out.File
	file_console_config_proto_rawDesc = nil
	file_console_config_proto_goTypes = nil
	file_console_config_proto_depIdxs = nil
}
