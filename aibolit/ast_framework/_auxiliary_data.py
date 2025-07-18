# SPDX-FileCopyrightText: Copyright (c) 2019-2025 Aibolit
# SPDX-License-Identifier: MIT

from typing import Dict, Set, Type, NamedTuple

from javalang import tree
from javalang.ast import Node

from aibolit.ast_framework import ASTNodeType


class ASTNodeReference(NamedTuple):
    node_index: int


javalang_to_ast_node_type: Dict[Type[Node], ASTNodeType] = {
    tree.Annotation: ASTNodeType.ANNOTATION,
    tree.AnnotationDeclaration: ASTNodeType.ANNOTATION_DECLARATION,
    tree.AnnotationMethod: ASTNodeType.ANNOTATION_METHOD,
    tree.ArrayCreator: ASTNodeType.ARRAY_CREATOR,
    tree.ArrayInitializer: ASTNodeType.ARRAY_INITIALIZER,
    tree.ArraySelector: ASTNodeType.ARRAY_SELECTOR,
    tree.AssertStatement: ASTNodeType.ASSERT_STATEMENT,
    tree.Assignment: ASTNodeType.ASSIGNMENT,
    tree.BasicType: ASTNodeType.BASIC_TYPE,
    tree.BinaryOperation: ASTNodeType.BINARY_OPERATION,
    tree.BlockStatement: ASTNodeType.BLOCK_STATEMENT,
    tree.BreakStatement: ASTNodeType.BREAK_STATEMENT,
    tree.Cast: ASTNodeType.CAST,
    tree.CatchClause: ASTNodeType.CATCH_CLAUSE,
    tree.CatchClauseParameter: ASTNodeType.CATCH_CLAUSE_PARAMETER,
    tree.ClassCreator: ASTNodeType.CLASS_CREATOR,
    tree.ClassDeclaration: ASTNodeType.CLASS_DECLARATION,
    tree.ClassReference: ASTNodeType.CLASS_REFERENCE,
    tree.CompilationUnit: ASTNodeType.COMPILATION_UNIT,
    tree.ConstantDeclaration: ASTNodeType.CONSTANT_DECLARATION,
    tree.ConstructorDeclaration: ASTNodeType.CONSTRUCTOR_DECLARATION,
    tree.ContinueStatement: ASTNodeType.CONTINUE_STATEMENT,
    tree.Creator: ASTNodeType.CREATOR,
    tree.Declaration: ASTNodeType.DECLARATION,
    tree.Documented: ASTNodeType.DOCUMENTED,
    tree.DoStatement: ASTNodeType.DO_STATEMENT,
    tree.ElementArrayValue: ASTNodeType.ELEMENT_ARRAY_VALUE,
    tree.ElementValuePair: ASTNodeType.ELEMENT_VALUE_PAIR,
    tree.EnhancedForControl: ASTNodeType.ENHANCED_FOR_CONTROL,
    tree.EnumBody: ASTNodeType.ENUM_BODY,
    tree.EnumConstantDeclaration: ASTNodeType.ENUM_CONSTANT_DECLARATION,
    tree.EnumDeclaration: ASTNodeType.ENUM_DECLARATION,
    tree.ExplicitConstructorInvocation: ASTNodeType.EXPLICIT_CONSTRUCTOR_INVOCATION,
    tree.Expression: ASTNodeType.EXPRESSION,
    tree.FieldDeclaration: ASTNodeType.FIELD_DECLARATION,
    tree.ForControl: ASTNodeType.FOR_CONTROL,
    tree.FormalParameter: ASTNodeType.FORMAL_PARAMETER,
    tree.ForStatement: ASTNodeType.FOR_STATEMENT,
    tree.IfStatement: ASTNodeType.IF_STATEMENT,
    tree.Import: ASTNodeType.IMPORT,
    tree.InferredFormalParameter: ASTNodeType.INFERRED_FORMAL_PARAMETER,
    tree.InnerClassCreator: ASTNodeType.INNER_CLASS_CREATOR,
    tree.InterfaceDeclaration: ASTNodeType.INTERFACE_DECLARATION,
    tree.Invocation: ASTNodeType.INVOCATION,
    tree.LambdaExpression: ASTNodeType.LAMBDA_EXPRESSION,
    tree.Literal: ASTNodeType.LITERAL,
    tree.LocalVariableDeclaration: ASTNodeType.LOCAL_VARIABLE_DECLARATION,
    tree.Member: ASTNodeType.MEMBER,
    tree.MemberReference: ASTNodeType.MEMBER_REFERENCE,
    tree.MethodDeclaration: ASTNodeType.METHOD_DECLARATION,
    tree.MethodInvocation: ASTNodeType.METHOD_INVOCATION,
    tree.MethodReference: ASTNodeType.METHOD_REFERENCE,
    tree.PackageDeclaration: ASTNodeType.PACKAGE_DECLARATION,
    tree.Primary: ASTNodeType.PRIMARY,
    tree.ReferenceType: ASTNodeType.REFERENCE_TYPE,
    tree.ReturnStatement: ASTNodeType.RETURN_STATEMENT,
    tree.Statement: ASTNodeType.STATEMENT,
    tree.StatementExpression: ASTNodeType.STATEMENT_EXPRESSION,
    tree.SuperConstructorInvocation: ASTNodeType.SUPER_CONSTRUCTOR_INVOCATION,
    tree.SuperMemberReference: ASTNodeType.SUPER_MEMBER_REFERENCE,
    tree.SuperMethodInvocation: ASTNodeType.SUPER_METHOD_INVOCATION,
    tree.SwitchStatement: ASTNodeType.SWITCH_STATEMENT,
    tree.SwitchStatementCase: ASTNodeType.SWITCH_STATEMENT_CASE,
    tree.SynchronizedStatement: ASTNodeType.SYNCHRONIZED_STATEMENT,
    tree.TernaryExpression: ASTNodeType.TERNARY_EXPRESSION,
    tree.This: ASTNodeType.THIS,
    tree.ThrowStatement: ASTNodeType.THROW_STATEMENT,
    tree.TryResource: ASTNodeType.TRY_RESOURCE,
    tree.TryStatement: ASTNodeType.TRY_STATEMENT,
    tree.Type: ASTNodeType.TYPE,
    tree.TypeArgument: ASTNodeType.TYPE_ARGUMENT,
    tree.TypeDeclaration: ASTNodeType.TYPE_DECLARATION,
    tree.TypeParameter: ASTNodeType.TYPE_PARAMETER,
    tree.VariableDeclaration: ASTNodeType.VARIABLE_DECLARATION,
    tree.VariableDeclarator: ASTNodeType.VARIABLE_DECLARATOR,
    tree.VoidClassReference: ASTNodeType.VOID_CLASS_REFERENCE,
    tree.WhileStatement: ASTNodeType.WHILE_STATEMENT,
}

common_attributes: Set[str] = {'node_type'}

attributes_by_node_type: Dict[ASTNodeType, Set[str]] = {
    ASTNodeType.ANNOTATION_DECLARATION: {
        'annotations',
        'body',
        'documentation',
        'modifiers',
        'name',
    },
    ASTNodeType.ANNOTATION_METHOD: {
        'annotations',
        'default',
        'dimensions',
        'modifiers',
        'name',
        'return_type',
    },
    ASTNodeType.ANNOTATION: {'element', 'name'},
    ASTNodeType.ARRAY_CREATOR: {
        'dimensions',
        'initializer',
        'postfix_operators',
        'prefix_operators',
        'qualifier',
        'selectors',
        'type',
    },
    ASTNodeType.ARRAY_INITIALIZER: {'initializers'},
    ASTNodeType.ARRAY_SELECTOR: {'index'},
    ASTNodeType.ASSERT_STATEMENT: {'condition', 'label', 'value'},
    ASTNodeType.ASSIGNMENT: {'expressionl', 'type', 'value'},
    ASTNodeType.BASIC_TYPE: {'dimensions', 'name'},
    ASTNodeType.BINARY_OPERATION: {'operandl', 'operandr', 'operator'},
    ASTNodeType.BLOCK_STATEMENT: {'label', 'statements'},
    ASTNodeType.BREAK_STATEMENT: {'goto', 'label'},
    ASTNodeType.CAST: {'expression', 'type'},
    ASTNodeType.CATCH_CLAUSE_PARAMETER: {'annotations', 'name', 'modifiers', 'types'},
    ASTNodeType.CATCH_CLAUSE: {'block', 'label', 'parameter'},
    ASTNodeType.CLASS_CREATOR: {
        'arguments',
        'body',
        'constructor_type_arguments',
        'postfix_operators',
        'prefix_operators',
        'qualifier',
        'selectors',
        'type',
    },
    ASTNodeType.CLASS_DECLARATION: {
        'annotations',
        'body',
        'documentation',
        'extends',
        'implements',
        'modifiers',
        'name',
        'type_parameters',
    },
    ASTNodeType.CLASS_REFERENCE: {
        'postfix_operators',
        'prefix_operators',
        'qualifier',
        'selectors',
        'type',
    },
    ASTNodeType.COLLECTION: set(),
    ASTNodeType.COMPILATION_UNIT: {'imports', 'package', 'types'},
    ASTNodeType.CONSTANT_DECLARATION: {
        'annotations',
        'declarators',
        'documentation',
        'modifiers',
        'type',
    },
    ASTNodeType.CONSTRUCTOR_DECLARATION: {
        'annotations',
        'body',
        'documentation',
        'modifiers',
        'name',
        'parameters',
        'throws',
        'type_parameters',
    },
    ASTNodeType.CONTINUE_STATEMENT: {'goto', 'label'},
    ASTNodeType.CREATOR: {
        'postfix_operators',
        'prefix_operators',
        'qualifier',
        'selectors',
        'type',
    },
    ASTNodeType.DECLARATION: {'annotations', 'modifiers'},
    ASTNodeType.DO_STATEMENT: {'body', 'condition', 'label'},
    ASTNodeType.DOCUMENTED: {'documentation'},
    ASTNodeType.ELEMENT_ARRAY_VALUE: {'values'},
    ASTNodeType.ELEMENT_VALUE_PAIR: {'name', 'value'},
    ASTNodeType.ENHANCED_FOR_CONTROL: {'iterable', 'var'},
    ASTNodeType.ENUM_BODY: {'constants', 'declarations'},
    ASTNodeType.ENUM_CONSTANT_DECLARATION: {
        'annotations',
        'arguments',
        'body',
        'documentation',
        'modifiers',
        'name',
    },
    ASTNodeType.ENUM_DECLARATION: {
        'annotations',
        'body',
        'documentation',
        'implements',
        'modifiers',
        'name',
    },
    ASTNodeType.EXPLICIT_CONSTRUCTOR_INVOCATION: {
        'arguments',
        'postfix_operators',
        'prefix_operators',
        'qualifier',
        'selectors',
        'type_arguments',
    },
    ASTNodeType.EXPRESSION: set(),
    ASTNodeType.FIELD_DECLARATION: {
        'annotations',
        'declarators',
        'documentation',
        'modifiers',
        'type',
    },
    ASTNodeType.FOR_CONTROL: {'condition', 'init', 'update'},
    ASTNodeType.FOR_STATEMENT: {'body', 'control', 'label'},
    ASTNodeType.FORMAL_PARAMETER: {
        'annotations',
        'modifiers',
        'name',
        'type',
        'varargs',
    },
    ASTNodeType.IF_STATEMENT: {
        'condition',
        'else_statement',
        'label',
        'then_statement',
    },
    ASTNodeType.IMPORT: {'path', 'static', 'wildcard'},
    ASTNodeType.INFERRED_FORMAL_PARAMETER: {'name'},
    ASTNodeType.INNER_CLASS_CREATOR: {
        'arguments',
        'body',
        'constructor_type_arguments',
        'postfix_operators',
        'prefix_operators',
        'qualifier',
        'selectors',
        'type',
    },
    ASTNodeType.INTERFACE_DECLARATION: {
        'annotations',
        'body',
        'documentation',
        'extends',
        'modifiers',
        'name',
        'type_parameters',
    },
    ASTNodeType.INVOCATION: {
        'arguments',
        'postfix_operators',
        'prefix_operators',
        'qualifier',
        'selectors',
        'type_arguments',
    },
    ASTNodeType.LAMBDA_EXPRESSION: {'body', 'parameters'},
    ASTNodeType.LITERAL: {
        'postfix_operators',
        'prefix_operators',
        'qualifier',
        'selectors',
        'value',
    },
    ASTNodeType.LOCAL_VARIABLE_DECLARATION: {
        'annotations',
        'declarators',
        'modifiers',
        'type',
    },
    ASTNodeType.MEMBER_REFERENCE: {
        'member',
        'postfix_operators',
        'prefix_operators',
        'qualifier',
        'selectors',
    },
    ASTNodeType.MEMBER: {'documentation'},
    ASTNodeType.METHOD_DECLARATION: {
        'annotations',
        'body',
        'documentation',
        'modifiers',
        'name',
        'parameters',
        'return_type',
        'throws',
        'type_parameters',
    },
    ASTNodeType.METHOD_INVOCATION: {
        'arguments',
        'member',
        'postfix_operators',
        'prefix_operators',
        'qualifier',
        'selectors',
        'type_arguments',
    },
    ASTNodeType.METHOD_REFERENCE: {'expression', 'method', 'type_arguments'},
    ASTNodeType.PACKAGE_DECLARATION: {
        'annotations',
        'documentation',
        'modifiers',
        'name',
    },
    ASTNodeType.PRIMARY: {
        'postfix_operators',
        'prefix_operators',
        'qualifier',
        'selectors',
    },
    ASTNodeType.REFERENCE_TYPE: {'arguments', 'dimensions', 'name', 'sub_type'},
    ASTNodeType.RETURN_STATEMENT: {'expression', 'label'},
    ASTNodeType.STATEMENT_EXPRESSION: {'expression', 'label'},
    ASTNodeType.STATEMENT: {'label'},
    ASTNodeType.STRING: {'string'},
    ASTNodeType.SUPER_CONSTRUCTOR_INVOCATION: {
        'arguments',
        'postfix_operators',
        'prefix_operators',
        'qualifier',
        'selectors',
        'type_arguments',
    },
    ASTNodeType.SUPER_MEMBER_REFERENCE: {
        'member',
        'postfix_operators',
        'prefix_operators',
        'qualifier',
        'selectors',
    },
    ASTNodeType.SUPER_METHOD_INVOCATION: {
        'arguments',
        'member',
        'postfix_operators',
        'prefix_operators',
        'qualifier',
        'selectors',
        'type_arguments',
    },
    ASTNodeType.SWITCH_STATEMENT_CASE: {'case', 'statements'},
    ASTNodeType.SWITCH_STATEMENT: {'cases', 'expression', 'label'},
    ASTNodeType.SYNCHRONIZED_STATEMENT: {'block', 'label', 'lock'},
    ASTNodeType.TERNARY_EXPRESSION: {'condition', 'if_false', 'if_true'},
    ASTNodeType.THIS: {
        'postfix_operators',
        'prefix_operators',
        'qualifier',
        'selectors',
    },
    ASTNodeType.THROW_STATEMENT: {'expression', 'label'},
    ASTNodeType.TRY_RESOURCE: {'annotations', 'name', 'modifiers', 'type', 'value'},
    ASTNodeType.TRY_STATEMENT: {
        'block',
        'catches',
        'finally_block',
        'label',
        'resources',
    },
    ASTNodeType.TYPE_ARGUMENT: {'pattern_type', 'type'},
    ASTNodeType.TYPE_DECLARATION: {
        'annotations',
        'body',
        'documentation',
        'modifiers',
        'name',
    },
    ASTNodeType.TYPE_PARAMETER: {'extends', 'name'},
    ASTNodeType.TYPE: {'dimensions', 'name'},
    ASTNodeType.VARIABLE_DECLARATION: {
        'annotations',
        'declarators',
        'modifiers',
        'type',
    },
    ASTNodeType.VARIABLE_DECLARATOR: {'dimensions', 'initializer', 'name'},
    ASTNodeType.VOID_CLASS_REFERENCE: {
        'postfix_operators',
        'prefix_operators',
        'qualifier',
        'selectors',
        'type',
    },
    ASTNodeType.WHILE_STATEMENT: {'body', 'condition', 'label'},
}
