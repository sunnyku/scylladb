include(generate_cql_grammar)
generate_cql_grammar(
  GRAMMAR expressions.g
  SOURCES cql_grammar_srcs)

add_library(alternator STATIC)
target_sources(alternator
  PRIVATE
    controller.cc
    server.cc
    executor.cc
    stats.cc
    serialization.cc
    expressions.cc
    conditions.cc
    auth.cc
    streams.cc
    ttl.cc
    ${cql_grammar_srcs})
target_include_directories(alternator
  PUBLIC
    ${CMAKE_SOURCE_DIR}
    ${CMAKE_BINARY_DIR})
target_link_libraries(alternator
  cql3
  idl
  Seastar::seastar
  xxHash::xxhash)
